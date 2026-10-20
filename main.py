import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.main_db import init_db
from handlers import commands, fsm_book

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    await init_db()
    
    dp.include_router(fsm_book.router_fsm)
    dp.include_router(commands.router_commands)
    
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())