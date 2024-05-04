from aiogram import Router, F
from .start import start_handler
from .start import get_pass
from .message import title_handler
from .dictionary import dictionary_handler, position, prev_page, next_page, get_video
from aiogram.filters import CommandStart, StateFilter
from states import UserState

router = Router()

router.message.register(start_handler, CommandStart())
router.message.register(get_pass, StateFilter(UserState.password))
router.message.register(dictionary_handler, StateFilter(
    UserState.search), F.text == "Словарь")
router.message.register(title_handler, StateFilter(
    UserState.search), F.text.regexp("^(?!/).*"))

router.callback_query.register(position, F.data == "position")
router.callback_query.register(prev_page, F.data.regexp(r"prev_.+"))
router.callback_query.register(next_page, F.data.regexp(r"next_.+"))
router.callback_query.register(get_video, F.data.regexp(r"id_.+"))
