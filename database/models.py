import enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import BIGINT, String, Text, VARCHAR, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = "User"

    id: Mapped[BIGINT] = mapped_column(BIGINT, primary_key=True)
    username: Mapped[String] = mapped_column(String(32))
    role: Mapped[UserRole]
    level_1: Mapped[bool] = mapped_column(default=False)
    level_2: Mapped[bool] = mapped_column(default=False)


class Words(Base):
    __tablename__ = "Words"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=False)
    file_id: Mapped[str] = mapped_column(Text, primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(50))
    level: Mapped[int] = mapped_column(SmallInteger)
