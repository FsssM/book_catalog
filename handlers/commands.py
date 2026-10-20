from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import main_db

router_commands = Router()

@router_commands.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в бот «Каталог книг»!\n\n"
        "Доступные команды:\n"
        "/add_book — Добавить новую книгу в базу\n"
        "/books — Посмотреть весь каталог книг"
    )

@router_commands.message(Command("books"))
async def cmd_books(message: Message):
    books = await main_db.get_catalog_from_db()
    
    if not books:
        await message.answer(" Каталог книг пока пуст. Добавьте первую книгу с помощью /add_book!")
        return

    for row in books:
        text = (
            f"**ID Книги:** {row['book_id']}\n"
            f"**Название:** {row['title']}\n"
            f"**Автор:** {row['author']}\n"
            f"**Жанр:** {row['genre']}\n"
            f"------------------------"
        )
        await message.answer(text)