# Manages configuration settings (e.g., API keys, database URLs)

from pydantic import BaseSettings

class Settings(BaseSettings):
    LLM_API_KEY: str
    LLM_API_URL: str = "https://api.mistral.ai/endpoint"  # Replace with the actual endpoint if needed
    MODERATION_THRESHOLD: float = 0.8

    class Config:
        env_file = ".env"

settings = Settings()