import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import user_router, admin_router
from loguru import logger

logger.add('logs/log_{time}.txt', rotation="12:00",
           format="{time} {level} {message}", compression="zip")

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@logger.catch
async def main():
    dp.include_routers(user_router, admin_router)
    logger.info("bot start polling")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main=main())
