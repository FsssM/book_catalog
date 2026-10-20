import aiosqlite
from database import queries
from config import path_db

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.CREATE_BOOKS_TABLE)
        await conn.execute(queries.CREATE_BOOKS_DETAIL_TABLE)
        await conn.commit()
    print("База данных успешно подключена")

async def save_book_to_db(book_id: int, title: str, author: str, genre: str):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.INSERT_BOOK, (book_id, title, author))
        await conn.execute(queries.INSERT_BOOK_DETAIL, (book_id, genre))
        await conn.commit()

async def get_catalog_from_db():
    async with aiosqlite.connect(path_db) as conn:
        conn.row_factory = aiosqlite.Row
        async with conn.execute(queries.SELECT_ALL_BOOKS_WITH_JOIN) as cursor:
            return await cursor.fetchall()