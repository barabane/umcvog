from database.db import session_maker
from sqlalchemy import insert, select


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            res = await session.execute(query)
            return res.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
