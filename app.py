import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI(title="NaijaLingua API",
             description="Enterprise-grade English to Yoruba, Igbo, and Hausa Translation Gateway")

tokenizer = None
model = None
MODEL_ID = "HelpMumHQ/AI-translator-eng-to-9ja"

@app.on_event("startup")
def load_model():
    global tokenizer, model
    print("Loading engine...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)

class TranslationRequest(BaseModel):
    text: str
    target_lang: Optional[str] = "yo" # Default to Yoruba

@app.post("/translate")
def translate_text(payload: TranslationRequest):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text empty.")
    
    # Force language selection
    valid_langs = ["yo", "ig", "ha"]
    lang = payload.target_lang if payload.target_lang in valid_langs else "yo"
    
    inputs = tokenizer(payload.text, return_tensors="pt", padding=True)
    
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs, 
            forced_bos_token_id=tokenizer.get_lang_id(lang), 
            max_length=256
        )
        
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    
    return {
        "status": "success",
        "translated_text": translated_text,
        "language_used": lang
    }

@app.get("/")
def health():
    return {"status": "active", "supported_languages": ["yo", "ig", "ha"]}