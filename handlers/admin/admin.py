import logging
from aiogram import types
from aiogram.utils.formatting import as_marked_section, Bold, as_key_value
from loguru import logger


@logger.catch
async def admin_handler(msg: types.Message):
    logger.info(f"Admin {msg.from_user.id} open admin panel")
    content = as_marked_section(
        Bold("Панель администратора"),
        as_key_value("/add", "добавить новое видео"),
        as_key_value("/exit", "выйти из админ. панели"),
        marker=""
    )
    await msg.answer(**content.as_kwargs())
