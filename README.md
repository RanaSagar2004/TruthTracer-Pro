# TruthTracer Pro

TruthTracer Pro is a **containerized demo application** that combines a FastAPI backend and a React frontend to demonstrate model inference, API integration, and full-stack deployment using Docker Compose. The backend integrates with a Hugging Face transformer model (`flan-t5-small`) to generate simple text predictions, and the frontend provides a clean interface for submitting claims and viewing results.

---

## Features

- **FastAPI backend**
  - Exposes REST API endpoints (`/api/predict`, `/api/analyze`).
  - Supports Hugging Face models with configurable environment variables.
  - Includes CORS middleware for browser access.
- **React frontend**
  - Built with React and served through Nginx.
  - Communicates with backend API via reverse proxy.
  - Provides an interface for submitting claims and displaying predictions.
- **Containerization**
  - Fully managed with Docker Compose.
  - Reproducible builds for both frontend and backend.
  - Configurable volumes for caching Hugging Face models.

---

## Architecture

csharp
Copy code
                ┌─────────────────┐
                │   React (UI)    │
                │   served by     │
Browser ───────►│   Nginx         │
                └───────┬─────────┘
                        │  /api/*
                        ▼
                ┌─────────────────┐
                │  FastAPI (API)  │
                │  Hugging Face   │
                │  model backend  │
                └─────────────────┘


markdown
Copy code

- **Frontend**: Runs on `http://localhost:3000`  
- **Backend**: API available on `http://localhost:8000`

---

## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)

### Setup

Clone the repository:
```bash
git clone https://github.com/<your-username>/truthtracer-pro.git
cd truthtracer-pro
Build and run the containers:

bash
Copy code
docker-compose up -d --build
The following services will start:

Frontend: http://localhost:3000

Backend API docs: http://localhost:8000/docs

API Endpoints
POST /api/predict
Runs inference on the provided text.

Request

json
Copy code
{
  "text": "Summarize: Artificial intelligence is changing industries.",
  "max_length": 60
}
Response

json
Copy code
{
  "input": "Summarize: Artificial intelligence is changing industries.",
  "prediction": "AI is transforming industries through automation and insights."
}
POST /api/analyze
Alias endpoint (same as /api/predict). Provided for frontend compatibility.

Environment Variables
Variable	Default	Description
USE_REAL_MODEL	true	Set to false to use a stubbed demo mode.
HF_MODEL	google/flan-t5-small	Hugging Face model identifier to load.
LOCAL_MODEL	same as HF_MODEL	Local model fallback.

Development
Rebuild the containers after making changes:

bash
Copy code
docker-compose build
docker-compose up -d
View logs:

bash
Copy code
docker-compose logs -f backend
docker-compose logs -f frontend
Stop services:

bash
Copy code
docker-compose down
Example Test
Using PowerShell:

powershell
Copy code
Invoke-RestMethod -Uri "http://localhost:3000/api/predict" `
  -Method POST `
  -ContentType "application/json" `
  -Body (@{ text = "Question: What color is the sky?"; max_length = 20 } | ConvertTo-Json)
Project Structure
bash
Copy code
truthtracer-pro/
├── backend/               # FastAPI application
│   ├── app/
│   │   └── main.py        # API entrypoint
│   └── Dockerfile
├── frontend/              # React app
│   ├── src/               # Frontend code
│   ├── nginx.conf         # Nginx reverse proxy config
│   └── Dockerfile
├── docker-compose.yml     # Service definitions
└── README.md              # Project documentation
License
This project is for demonstration purposes only.
