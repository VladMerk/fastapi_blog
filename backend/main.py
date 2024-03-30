from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)


@app.get("/")
async def hello_api() -> dict[str, str]:
    return {"message": "Hello FastAPI"}