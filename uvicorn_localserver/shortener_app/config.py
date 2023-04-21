# shortener_app/config.py


from functools import lru_cache
from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

class Settings(BaseSettings):

    env_name: str = os.environ.get("ENV_NAME", "Local")
    
    base_url: str = os.environ.get("BASE_URL", "http://localhost:8000")

    db_url: str = "sqlite:///./shortener.db"
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:

    settings = Settings()

    print(f"Loading settings for: {settings.env_name}")

    return settings
