from .Base import Base
from sqlalchemy import Text, VARCHAR, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Video(Base):
    __tablename__ = "Video"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True)
    file_id: Mapped[str] = mapped_column(Text)
    title: Mapped[str] = mapped_column(VARCHAR(50))
