from aiogram import Router, F
from .start import start_handler
from .start import get_pass
from .message import title_handler
from aiogram.filters import CommandStart, StateFilter
from states import UserState

router = Router()

router.message.register(start_handler, CommandStart())
router.message.register(get_pass, StateFilter(UserState.password))
router.message.register(title_handler, StateFilter(
    UserState.search), F.text.regexp("^(?!/).*"))
