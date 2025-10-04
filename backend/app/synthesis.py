import os, random
from datetime import datetime

USE_REAL_MODEL = os.getenv("USE_REAL_MODEL", "false").lower() == "true"

def synthesize_verdict(claim: str, sources: list):
    # Calculate average reliability
    avg_rel = sum(s["reliability"] for s in sources) / len(sources)
    confidence = int(avg_rel * 100)
    if confidence > 70:
        verdict = "Likely True"
    elif confidence >= 50:
        verdict = "Mixed / Inconclusive"
    else:
        verdict = "Likely False"

    summary = f"Automated synthesis (mock). Verdict: {verdict}, confidence {confidence}%."

    # Timeline
    timeline = sorted(
        [{"date": s["date"], "event": f"{s['id']}: {s['title']}"} for s in sources],
        key=lambda x: x["date"]
    )

    # Provenance
    provenance = [
        {"source": s["id"], "quote": s["snippet"], "loc": "paragraph 1"} for s in sources
    ]

    return {
        "claim": claim,
        "verdict": verdict,
        "confidence": confidence,
        "summary": summary,
        "sources": sources,
        "timeline": timeline,
        "provenance": provenance,
        "notes": "Mock synthesis. Set USE_REAL_MODEL=true to enable HuggingFace pipeline."
    }
