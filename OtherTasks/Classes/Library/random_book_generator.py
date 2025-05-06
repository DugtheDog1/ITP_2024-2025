from random import randint
from models import Book


books = []

for x in range(100):
    book_title = f"Book Title {x}"
    book_author = f"Book Author {x}"
    book_id = randint(1, 12000)
    shelf_num = x + 1
    books.append(Book(book_title, book_author, book_id, shelf_num))


