from aiogram import types
from database import db
from fuzzywuzzy import fuzz
from loguru import logger


async def title_handler(msg: types.Message):
    logger.info(f"User {msg.from_user.id} searching for {msg.text}")
    videos = db.get_video(msg.text)

    if videos == []:
        return await msg.answer("Ничего не найдено 😔 Попробуйте еще раз")

    for video in videos:
        if fuzz.token_sort_ratio(video.title, msg.text) >= 50:
            await msg.answer_video(video.file_id, caption=video.title)
