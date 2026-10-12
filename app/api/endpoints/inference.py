import time
import numpy as np
from fastapi import APIRouter, HTTPException
from app.schemas.payload import InferenceRequest, InferenceResponse
from app.core.engine import ONNXInferenceEngine
from app.config import settings

router = APIRouter()
engine = ONNXInferenceEngine(settings.MODEL_PATH)

@router.post("/predict", response_model=InferenceResponse)
async def predict(payload: InferenceRequest):
    start_time = time.perf_counter()
    
    try:
        # For now, convert string length or mock features based on the text
        dummy_features = [float(len(payload.text)), 1.0, 0.5]
        input_data = np.array([dummy_features], dtype=np.float32)
        
        result = engine.predict(input_data)
        latency = (time.perf_counter() - start_time) * 1000
        
        return InferenceResponse(
            success=True,
            predictions=result["predictions"],
            shape=list(result["shape"]),
            latency_ms=round(latency, 2),
            execution_type=result["status"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference execution failed: {str(e)}")