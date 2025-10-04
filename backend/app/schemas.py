from pydantic import BaseModel
from typing import Optional, List

class AnalyzeRequest(BaseModel):
    text: Optional[str]

class Source(BaseModel):
    id: str
    title: str
    url: str
    date: Optional[str]
    snippet: Optional[str]
    reliability: Optional[float]

class TimelineItem(BaseModel):
    date: str
    event: str

class ProvenanceItem(BaseModel):
    source: str
    quote: str
    loc: Optional[str]

class AnalyzeResponse(BaseModel):
    claim: str
    verdict: str
    confidence: int
    summary: str
    sources: List[Source]
    timeline: List[TimelineItem]
    provenance: List[ProvenanceItem]
    notes: Optional[str]
