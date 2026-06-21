# NaijaLingua API

A high-performance, multilingual translation gateway designed for Nigerian regional languages. Built with FastAPI and transformer models to bridge the gap between English and indigenous Nigerian languages.

## 🌍 Supported Languages
- **Yoruba** (`yo`)
- **Igbo** (`ig`)
- **Hausa** (`ha`)

## 🚀 Quick Start
Integrate this API into your application by sending a `POST` request to the `/translate` endpoint.

### Example Request
```json
{
  "text": "Register your business today.",
  "target_lang": "yo"
}
````
### Example Response
```json
{
  "status": "success",
  "translated_text": "Forúkọọ́wọ́ iṣẹ́ rẹ lónìí.",
  "language_used": "yo"
}
```

🛠️ Tech Stack
Framework: FastAPI

Model Engine: Transformer-based sequence-to-sequence model

Deployment: Hugging Face Spaces (CI/CD via GitHub Actions)

📋 API Documentation
For full technical documentation and interactive testing, visit the API Docs:
https://abidemiadetula-yoruba-translation-api.hf.space/docs

Built to power localized Nigerian digital infrastructure.
