import os
from dao.base import BaseDAO
from sqlalchemy import func, select, case
from database.db import session_maker
from database.models import User, Words


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def find_words_like(cls, title: str):
        async with session_maker() as session:
            query = select(Words).where(Words.title.like(
                f"{title}%")).where(Words.level == int(os.getenv("LEVEL")))
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def get_words(cls, offset: int = 1, limit: int = 10):
        async with session_maker() as session:
            query = select(Words).where(Words.level == int(os.getenv("LEVEL"))).order_by(
                case((Words.title.regexp_match("^[0-9]"), 2), else_=1), Words.title).offset((offset - 1) * limit).limit(limit)
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def get_words_quantity(cls):
        async with session_maker() as session:
            query = select(func.count()).select_from(
                Words).where(Words.level == int(os.getenv("LEVEL")))
            res = await session.execute(query)
            return res.scalar()

    @classmethod
    async def find_word_by_id(cls, word_id):
        async with session_maker() as session:
            query = select(Words).filter_by(id=word_id)
            res = await session.execute(query)
            return res.scalar_one_or_none()
