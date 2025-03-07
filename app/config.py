# Manages configuration settings (e.g., API keys, database URLs)

import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    LLM_API_KEY: str
    LLM_API_URL: str = "https://api.mistral.ai/endpoint"  # Replace with actual endpoint
    MODERATION_THRESHOLD: float = 0.8  # Probability threshold

    class Config:
        env_file = ".env"

settings = Settings()