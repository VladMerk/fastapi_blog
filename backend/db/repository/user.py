from sqlalchemy.ext.asyncio import AsyncSession
from core.hashing import Hasher
from db.models.users import User
from schemas.user import UserCreate


async def create_new_user(user_in: UserCreate, session: AsyncSession) -> User:
    user = User(
        email=user_in.email,
        password=Hasher.get_password_hash(user_in.password),
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user
