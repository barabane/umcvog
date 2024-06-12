from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from .admin import admin_handler
from .add import add_video, set_title, set_video, set_video_document
from .exit import admin_exit
from filters import AdminFilter
from states import AdminState

router = Router()

router.message.register(admin_handler, AdminFilter(), Command("admin"))
router.message.register(add_video, AdminFilter(), Command("add"))
router.message.register(set_title, StateFilter(AdminState.add))
router.message.register(set_video, StateFilter(
    AdminState.title), F.video)
router.message.register(set_video_document, StateFilter(
    AdminState.title), F.document.mime_type == "video/mp4")
router.message.register(admin_exit, Command("exit"), AdminFilter())
