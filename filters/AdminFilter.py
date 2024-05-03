from aiogram import types
from aiogram.filters import BaseFilter
from database import db


class AdminFilter(BaseFilter):
    async def __call__(self, msg: types.Message) -> bool:
        user = db.get_user(msg.from_user.id)
        if str(user.role.value) == "admin":
            return True
        return False
