from sqlalchemy import BIGINT, String
from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base, UserRole


class User(Base):
    __tablename__ = "User"

    id: Mapped[BIGINT] = mapped_column(BIGINT, primary_key=True)
    username: Mapped[String] = mapped_column(String(32))
    role: Mapped[UserRole]
