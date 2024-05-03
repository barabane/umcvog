import enum
from sqlalchemy.orm import DeclarativeBase


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"


class Base(DeclarativeBase):
    pass
