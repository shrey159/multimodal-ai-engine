from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Multimodal AI Inference Engine",
        "version": "1.0.0"
    }