# Multi-LLM Benchmarking Platform
## ⚡ Quick Setup

### 1. Clone & Install
```bash
git clone <your-repo-url>
cd llm_benchmark
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### 2. PostgreSQL Database Banao
```sql
CREATE DATABASE llm_benchmark_db;
```

### 3. `.env` File Banao
```env
SECRET_KEY=django-insecure-changeme
DB_NAME=llm_benchmark_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
OPENROUTER_API_KEY=your_openrouter_key
```

### 4. Migrate & Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔗 API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/evaluate/` | Prompt submit karo |
| GET | `/api/history/` | Saare past evaluations |
| GET | `/api/history/<id>/` | Specific session detail |
| GET | `/api/leaderboard/` | Model rankings |
| GET | `/swagger/` | Swagger UI docs |

## 📬 Sample Request

```bash
curl -X POST http://localhost:8000/api/evaluate/ \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain Django ORM in simple terms."}'
```
## 📬 Sample Response

```json
{
  "session_id": 1,
  "prompt": "Explain Django ORM in simple terms.",
  "winner": "Groq-llama-3.1-8b-instant",
  "final_score": 8.5,
  "all_responses": [
    {
      "label": "A",
      "model_name": "Groq-llama-3.1-8b-instant",
      "response_text": "Django ORM is...",
      "response_time_ms": 1234.5,
      "groq_score": 8,
      "gemini_score": 9,
      "final_score": 8.5
    }
  ]
}
```

## Architecture
```
User → POST /api/evaluate/
         ↓
    asyncio.gather() → [Groq LLaMA, Groq Qwen, OpenRouter x2] (parallel)
         ↓
    Anonymize responses (A, B, C, D)
         ↓
    asyncio.gather() → [Groq Judge, Gemini Judge] (parallel)
         ↓
    Average scores → Pick winner
         ↓
    Save to PostgreSQL → Return result
```
