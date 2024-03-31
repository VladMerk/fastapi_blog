from fastapi import FastAPI
from apis.v1 import route_users
from apps.v1 import route_blog
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)
app.include_router(route_users.router)
app.include_router(route_blog.router)


@app.get("/")
async def hello_api() -> dict[str, str]:
    return {"message": "Hello FastAPI"}
