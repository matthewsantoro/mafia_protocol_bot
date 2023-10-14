import asyncio
import logging
from aiogram import Bot, Dispatcher
import os
from handlers import games, different_types


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(games.router, different_types.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
