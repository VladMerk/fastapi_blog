from fastapi import HTTPException, status
from sqlalchemy import ScalarResult, select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from db.base import Base


class BaseCRUD:
    def __init__(self, model: type[Base]) -> None:
        self.model: type[Base] = model

    async def get_all(self, session: AsyncSession) -> list[Base]:
        result: ScalarResult = await session.scalars(select(self.model))
        return list(result.all())

    async def get_by_id(self, model_id: int, session: AsyncSession) -> Base | None:
        return await session.get(self.model, self.model.id == model_id)

    async def create(self, obj_in: BaseModel, session: AsyncSession) -> Base:
        db_obj = self.model(*obj_in.model_dump())

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj

    async def remove(self, model_id: int, session: AsyncSession) -> Base:
        obj: Base | None = await session.scalar(select(self.model).where(self.model.id == model_id))
        if obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__.capitalize()} with id={model_id} not found!",
            )

        await session.delete(obj)
        await session.commit()
        return obj
