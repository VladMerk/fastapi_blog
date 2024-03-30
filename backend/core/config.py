from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Blog"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.slite3"
    DB_ECHO: bool = True


settings = Settings()
