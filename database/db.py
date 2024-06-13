from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import DB_URL

engine = create_async_engine(
    DB_URL, pool_size=30, max_overflow=3, pool_recycle=3600, pool_timeout=5000)
session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)
