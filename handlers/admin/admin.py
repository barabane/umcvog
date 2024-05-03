from aiogram import types
from aiogram.utils.formatting import as_marked_section, Bold, as_key_value


async def admin_handler(msg: types.Message):
    content = as_marked_section(
        Bold("Панель администратора"),
        as_key_value("/add", "добавить новое видео"),
        as_key_value("/exit", "выйти из админ. панели"),
        marker=""
    )
    await msg.answer(**content.as_kwargs())
