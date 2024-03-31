from db.models.users import User
from db.repository.user import db_user
from db.session import session_dependency
from fastapi import APIRouter, Depends, Form
from schemas.user import ShowUser, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.get("/", response_model=list[ShowUser])
async def get_users(session: AsyncSession = Depends(session_dependency)) -> list[ShowUser]:
    users: list[User] = await db_user.get_all(session=session)
    return [ShowUser.model_validate(user) for user in users]


@router.post("/", response_model=ShowUser)
async def create_user(
    email: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(session_dependency),
) -> ShowUser:
    user_in = UserCreate(email=email, password=password)
    user: User = await db_user.create(user_in, session)
    return ShowUser.model_validate(user)


@router.delete("/{user_id}")
async def remove_user(
    user_id: int, session: AsyncSession = Depends(session_dependency)
) -> ShowUser:
    user: User = await db_user.remove(user_id, session)
    return ShowUser.model_validate(user)
