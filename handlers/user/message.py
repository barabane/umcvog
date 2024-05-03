from aiogram import types
from database import db
from fuzzywuzzy import fuzz


async def title_handler(msg: types.Message):
    videos = db.get_video(msg.text)

    if videos == []:
        return await msg.answer("Ничего не найдено 😔 Попробуйте еще раз")

    for video in videos:
        if fuzz.token_sort_ratio(video.title, msg.text) >= 50:
            await msg.answer_video(video.file_id, caption=video.title)
