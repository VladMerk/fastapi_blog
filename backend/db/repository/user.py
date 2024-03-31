from core.hashing import Hasher
from core.repository import BaseCRUD
from db.models.users import User
from schemas.user import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession


class UserCRUD(BaseCRUD[User, UserCreate, UserUpdate]):
    async def create(self, obj_in: UserCreate, session: AsyncSession) -> User:
        user = User(email=obj_in.email, password=Hasher.get_password_hash(obj_in.password))

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user


db_user = UserCRUD(User)
