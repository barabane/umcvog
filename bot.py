import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import user_router, admin_router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main=main())
