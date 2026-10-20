from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import main_db

router_fsm = Router()

class BookForm(StatesGroup):
    book_id = State()
    title = State()
    author = State()
    genre = State()

@router_fsm.message(Command("add_book"))
async def start_add_book(message: Message, state: FSMContext):
    await message.answer("Начинаем добавление книги.\nВведите уникальный номер (ID) книги:")
    await state.set_state(BookForm.book_id)

@router_fsm.message(BookForm.book_id)
async def process_book_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Номер книги должен быть числом. Введите ещё раз:")
        return
        
    await state.update_data(book_id=int(message.text))
    await message.answer("Введите название книги:")
    await state.set_state(BookForm.title)

@router_fsm.message(BookForm.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите автора книги:")
    await state.set_state(BookForm.author)

@router_fsm.message(BookForm.author)
async def process_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer("🎭 Введите жанр книги:")
    await state.set_state(BookForm.genre)

@router_fsm.message(BookForm.genre)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    
    await main_db.save_book_to_db(
        book_id=data["book_id"],
        title=data["title"],
        author=data["author"],
        genre=data["genre"]
    )
    
    summary = (
        "Книга успешно добавлена в базу данных!\n\n"
        f"ID: {data['book_id']}\n"
        f"Название: {data['title']}\n"
        f"Автор: {data['author']}\n"
        f"Жанр: {data['genre']}"
    )
    await message.answer(summary)
    await state.clear()