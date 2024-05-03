from aiogram import types
from aiogram.fsm.context import FSMContext
from database import db
from states import AdminState


async def add_video(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.add)
    await msg.answer("Напишите слово, по которому ученики будут искать видео:")


async def set_title(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.title)
    await state.set_data({'title': msg.text})
    await msg.answer("Теперь отправьте видео:")


async def set_video(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.video)
    data = await state.get_data()
    db.set_video(msg.video.file_id, data['title'])
    await msg.answer("Видео успешно добавлено!")


async def set_video_document(msg: types.Message, state: FSMContext):
    await state.set_state(AdminState.video)
    data = await state.get_data()
    db.set_video(msg.document.file_id, data['title'])
    await msg.answer("Видео успешно добавлено!")
    await state.clear()
