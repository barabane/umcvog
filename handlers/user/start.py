from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.user.dao import UserDAO
from states import UserState
from keyboards import dictionary_kb
from settings import PASS


async def start_handler(msg: types.Message, state: FSMContext):
    user = await UserDAO.find_one_or_none(id=msg.from_user.id)

    if not user:
        await state.set_state(UserState.password)
        return await msg.answer("Введите пароль для входа:")
    await state.set_state(UserState.search)
    return await msg.answer("Введите слово для поиска:", reply_markup=dictionary_kb())


async def get_pass(msg: types.Message, state: FSMContext):
    if msg.text != PASS:
        return await msg.answer("Неправильный пароль")
    await msg.answer("Добро пожаловать!")
    await UserDAO.add(
        id=msg.from_user.id,
        username=msg.from_user.username or '',
        role='user'
    )
    await state.set_state(UserState.search)
    await msg.answer("Введите слово для поиска:", reply_markup=dictionary_kb())
