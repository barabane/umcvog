from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import DB_URL

engine = create_async_engine(DB_URL)
session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)
