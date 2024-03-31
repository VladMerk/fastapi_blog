from db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__: str = "users"

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(server_default="TRUE", default=True)
