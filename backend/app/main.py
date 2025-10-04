import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from fastapi.middleware.cors import CORSMiddleware

USE_REAL = os.getenv("USE_REAL_MODEL", "false").lower() in ("1", "true", "yes")
HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-small")

app = FastAPI(title="TruthTracer Demo Backend")

# Enable CORS (so frontend at localhost:3000 works fine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],  # allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model only if using real mode
if USE_REAL:
    from .model import get_tokenizer_and_model
    try:
        tokenizer, model = get_tokenizer_and_model()
        DEVICE = next(model.parameters()).device
    except Exception as e:
        raise RuntimeError(f"Failed to load model {HF_MODEL}: {e}")
else:
    tokenizer = None
    model = None
    DEVICE = "cpu"

class PredictRequest(BaseModel):
    text: str
    max_length: int = 128
    num_beams: int = 4

@app.get("/")
async def root():
    return {"detail": "Backend up", "use_real_model": USE_REAL, "model": HF_MODEL}

# Main predict endpoint
@app.post("/api/predict")
async def predict(req: PredictRequest):
    if not req.text or not isinstance(req.text, str):
        raise HTTPException(status_code=400, detail="`text` must be a non-empty string")

    if not USE_REAL:
        return {
            "input": req.text,
            "prediction": f"DEMO: Received input of length {len(req.text)}. (Stubbed response)",
            "confidence": 0.75,
        }

    # Run real model
    inputs = tokenizer(
        req.text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_length=req.max_length,
            num_beams=req.num_beams,
            early_stopping=True
        )
    decoded = tokenizer.decode(out[0], skip_special_tokens=True)
    return {"input": req.text, "prediction": decoded}

# Alias endpoint for frontend
@app.post("/api/analyze")
async def analyze(req: PredictRequest):
    return await predict(req)
