# backend/app/model.py
import os
from functools import lru_cache
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-small")
CACHE_DIR = os.getenv("HF_CACHE_DIR", "/root/.cache/huggingface")

# choose device
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

@lru_cache()
def get_tokenizer_and_model():
    """
    Loads tokenizer and seq2seq model from Hugging Face. Cached for process lifetime.
    """
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL, cache_dir=CACHE_DIR, use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL, cache_dir=CACHE_DIR)
    model.to(DEVICE)
    model.eval()
    return tokenizer, model
