from aiogram import types
from aiogram.fsm.context import FSMContext
from states import UserState


async def admin_exit(msg: types.Message, state: FSMContext):
    await state.set_state(UserState.search)
    await msg.answer("Вы вышли из админ. панели")
