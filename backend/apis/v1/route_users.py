from typing import Sequence
from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreate, ShowUser
from db.models.users import User
from db.session import session_dependency
from db.repository.user import create_new_user


router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.get("/", response_model=list[ShowUser])
async def get_users(
    session: AsyncSession = Depends(session_dependency),
) -> list[ShowUser]:
    result: Result = await session.execute(select(User))
    users: Sequence[User] = result.scalars().all()
    return [ShowUser.model_validate(user) for user in users]


@router.post("/", response_model=ShowUser)
async def create_user(
    email: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(session_dependency),
) -> ShowUser:
    user_in = UserCreate(email=email, password=password)
    user: User = await create_new_user(user_in, session)
    return ShowUser.model_validate(user)
