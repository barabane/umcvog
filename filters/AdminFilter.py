from aiogram import types
from aiogram.filters import BaseFilter
from handlers.user.dao import UserDAO


class AdminFilter(BaseFilter):
    async def __call__(self, msg: types.Message) -> bool:
        user = await UserDAO.find_one_or_none(id=msg.from_user.id)
        if str(user.role.value) == "admin":
            return True
        return False
