import os
from dotenv import load_dotenv

from aiogram import types
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from .models import Video, User, Base

load_dotenv()


class DB:
    def __init__(self):
        self.__engine = create_engine(
            f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?charset=utf8mb4")
        self.__session = sessionmaker(bind=self.__engine)()
        self.__metadata = Base.metadata
        self.__metadata.create_all(bind=self.__engine)

    def get_user(self, id):
        return self.__session.get(User, id)

    def reg_user(self, user: types.User, role):
        if self.__session.get(User, user.id):
            return False

        new_user = User(
            id=user.id,
            username=user.username if user.username else "None",
            role=role
        )
        self.__session.add(new_user)
        self.__session.commit()
        return True

    def set_video(self, id, title):
        self.__session.add(Video(
            file_id=id,
            title=title
        ))
        self.__session.commit()

    def get_video(self, title):
        return self.__session.execute(select(Video).where(Video.title.contains(f"%{title}%"))).scalars().all()

    def get_video_by_id(self, id):
        return self.__session.get(Video, id)

    def get_videos_qntity(self):
        return len(self.__session.scalars(select(Video)).all())

    def get_videos(self, offset: int = 1, limit: int = 10):
        return self.__session.scalars(select(Video).offset((offset - 1) * limit).limit(limit)).all()


db = DB()
