import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from auth_student import start

config_file = open('config/config.txt', 'r')
token_bot = config_file.readline()
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=token_bot)
    dp = Dispatcher()

    dp.include_router(start.router)

    bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

config_file.close()
