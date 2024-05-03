from aiogram.fsm.state import StatesGroup, State


class AdminState(StatesGroup):
    add = State()
    title = State()
    video = State()
