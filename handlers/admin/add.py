import os
from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.admin.dao import AdminDAO
from states import AdminState
from loguru import logger


@logger.catch
async def add_video(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.add)
    await msg.answer("Напишите слово, по которому ученики будут искать видео:")


@logger.catch
async def set_title(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.title)
    await state.set_data({'title': msg.text})
    await msg.answer("Теперь отправьте видео:")


@logger.catch
async def set_video(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.video)
    data = await state.get_data()
    await AdminDAO.add_video(
        file_id=msg.video.file_id if msg.video else msg.document.file_id,
        title=data['title'],
        level=os.getenv("LEVEL")
    )
    await msg.answer("Видео успешно добавлено!")


@logger.catch
async def set_video_document(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.video)
    data = await state.get_data()
    await AdminDAO.add_video(
        file_id=msg.video.file_id if msg.video else msg.document.file_id,
        title=data['title'],
        level=os.getenv("LEVEL")
    )
    await msg.answer("Видео успешно добавлено!")
    await state.clear()
