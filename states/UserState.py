from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    password = State()
    search = State()
