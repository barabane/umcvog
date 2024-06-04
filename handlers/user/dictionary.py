from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.dictionary_kb import dictionary_kb
from database import db
from loguru import logger


@logger.catch
async def dictionary_handler(msg: types.Message, state: FSMContext):
    videos = db.get_videos()
    videos_qntity = db.get_videos_qntity()
    await msg.answer(text='Словарь', reply_markup=dictionary_kb(videos, 1, videos_qntity))


@logger.catch
async def prev_page(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    videos_qntity = db.get_videos_qntity()
    position = 0 if int(cq.data.split("_")[1]) < 0 else int(
        cq.data.split("_")[1])
    videos = db.get_videos(position - 1)
    await cq.message.edit_reply_markup(reply_markup=dictionary_kb(videos, position - 1, videos_qntity))


@logger.catch
async def next_page(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    videos_qntity = db.get_videos_qntity()
    position = int(cq.data.split("_")[1])
    videos = db.get_videos(position + 1)
    await cq.message.edit_reply_markup(reply_markup=dictionary_kb(videos, position + 1, videos_qntity))


async def position(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()


@logger.catch
async def get_video(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    video = db.get_video_by_id(int(cq.data.split("_")[1]))
    await cq.message.answer_video(video.file_id, caption=video.title)
