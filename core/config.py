from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = "postgresql+asyncpg://postgres:12345ver@localhost:5432/microshop_db"
    db_echo: bool = False


settings = Settings()
