import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_router, admin_router
from loguru import logger
from settings import TOKEN

logger.add('logs/log_{time}.txt', rotation="12:00",
           format="{time} {level} {message}", compression="zip")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@logger.catch
async def main():
    dp.include_routers(user_router, admin_router)
    logger.info("bot start polling")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main=main())
