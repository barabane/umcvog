from aiogram import types
from sqlalchemy import create_engine, select, case
from sqlalchemy.orm import sessionmaker
from .models import Video, User, Base
from loguru import logger
from settings import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


class DB:
    def __init__(self):
        self.__engine = create_engine(
            f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4")
        self.__session = sessionmaker(bind=self.__engine)()
        self.__metadata = Base.metadata
        self.__metadata.create_all(bind=self.__engine)

    @logger.catch
    def get_user(self, id: int):
        return self.__session.get(User, id)

    @logger.catch
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
        logger.success(f"User {new_user.id} just registered")
        return True

    @logger.catch
    def set_video(self, id, title):
        video = Video(
            file_id=id,
            title=title
        )

        self.__session.add(video)
        self.__session.commit()
        return video

    @logger.catch
    def get_video(self, title):
        return self.__session.execute(select(Video).where(Video.title.like(f"{title}%"))).scalars().all()

    @logger.catch
    def get_video_by_id(self, id):
        return self.__session.get(Video, id)

    @logger.catch
    def get_videos_qntity(self):
        return len(self.__session.scalars(select(Video)).all())

    @logger.catch
    def get_videos(self, offset: int = 1, limit: int = 10):
        return self.__session.query(Video).order_by(
            case((Video.title.regexp_match("^[0-9]"), 2), else_=1), Video.title
        ).offset((offset - 1) * limit).limit(limit).all()


db = DB()
