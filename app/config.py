from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Edge-Optimized Multimodal AI Engine"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    MODEL_PATH: str = "models/model.onnx"

    class Config:
        env_file = ".env"

settings = Settings()