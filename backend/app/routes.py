import os, random
from fastapi import APIRouter
from .schemas import AnalyzeRequest, AnalyzeResponse
from .retrieval import retrieve_sources
from .synthesis import synthesize_verdict

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    claim = req.text or "Eating carrots improves night vision."
    sources = retrieve_sources(claim)
    result = synthesize_verdict(claim, sources)
    return result
