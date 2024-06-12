from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.words_list_kb import words_list
from loguru import logger
from handlers.user.dao import UserDAO


@logger.catch
async def dictionary_handler(msg: types.Message, state: FSMContext):
    videos = await UserDAO.get_words()
    videos_qntity = await UserDAO.get_words_quantity()
    await msg.answer(text='Словарь', reply_markup=words_list(videos, 1, videos_qntity))


@logger.catch
async def prev_page(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    videos_qntity = await UserDAO.get_words_quantity()
    position = 0 if int(cq.data.split("_")[1]) < 0 else int(
        cq.data.split("_")[1])
    videos = await UserDAO.get_words(position - 1)
    await cq.message.edit_reply_markup(reply_markup=words_list(videos, position - 1, videos_qntity))


@logger.catch
async def next_page(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    videos_qntity = await UserDAO.get_words_quantity()
    position = int(cq.data.split("_")[1])
    videos = await UserDAO.get_words(position + 1)
    await cq.message.edit_reply_markup(reply_markup=words_list(videos, position + 1, videos_qntity))


async def position(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()


@logger.catch
async def get_video(cq: types.CallbackQuery, state: FSMContext):
    await cq.answer()
    video = await UserDAO.find_word_by_id(word_id=int(cq.data.split("_")[1]))
    await cq.message.answer_video(video.file_id, caption=video.title)
