from pydantic import BaseModel, Field
from typing import List, Optional

class InferenceRequest(BaseModel):
    text: str = Field(..., description="Input text string for processing")

class InferenceResponse(BaseModel):
    success: bool = True
    predictions: List[List[float]]
    shape: List[int]
    latency_ms: float
    execution_type: str