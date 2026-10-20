CREATE_BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER UNIQUE,
    title TEXT,
    author TEXT
)
"""

CREATE_BOOKS_DETAIL_TABLE = """
CREATE TABLE IF NOT EXISTS books_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    genre TEXT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)
"""

INSERT_BOOK = "INSERT INTO books (book_id, title, author) VALUES (?, ?, ?)"
INSERT_BOOK_DETAIL = "INSERT INTO books_detail (book_id, genre) VALUES (?, ?)"

SELECT_ALL_BOOKS_WITH_JOIN = """
SELECT b.book_id, b.title, b.author, d.genre
FROM books b
INNER JOIN books_detail d ON b.book_id = d.book_id
"""