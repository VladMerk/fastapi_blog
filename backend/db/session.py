from typing import AsyncGenerator

from core.config import settings
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)


engine: AsyncEngine = create_async_engine(url=settings.DB_URL, echo=settings.DB_ECHO)

session_factory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


async def session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
        await session.close()
