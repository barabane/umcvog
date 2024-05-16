from aiogram import types
from aiogram.fsm.context import FSMContext
from database.models.User import User
from states import UserState
from database import db
from keyboards import dictionary_kb
from settings import PASS


async def start_handler(msg: types.Message, state: FSMContext):
    user: User | None = db.get_user(msg.from_user.id)

    if user:
        if user.role == "admin":
            await msg.answer("У вас есть права администратора. Для того, чтобы перейти в панель администратора, введите команду /admin")
        await state.set_state(UserState.search)
        return await msg.answer("Введите слово для поиска:", reply_markup=dictionary_kb())
    await state.set_state(UserState.password)
    await msg.answer("Введите пароль для входа:")


async def get_pass(msg: types.Message, state: FSMContext):
    if msg.text != PASS:
        return await msg.answer("Неправильный пароль")
    await msg.answer("Добро пожаловать!")
    db.reg_user(msg.from_user, "user")
    await state.set_state(UserState.search)
    await msg.answer("Введите слово для поиска:", reply_markup=dictionary_kb())
