from dao.base import BaseDAO
from sqlalchemy import insert
from database.models import User, Words
from database.db import session_maker


class AdminDAO(BaseDAO):
    model = User

    @classmethod
    async def add_video(cls, **data):
        async with session_maker() as session:
            query = insert(Words).values(**data)
            res = await session.execute(query)
            await session.commit()
