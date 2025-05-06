from random import randint

class Book:
    def __init__(self, title, author, book_id, shelf_num):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.shelf_num = shelf_num

books = []

for x in range(100):
    book_title = f"Book Title {x}"
    book_author = f"Book Author {x}"
    book_id = randint(1, 12000)
    shelf_num = x + 1
    books.append(Book(book_title, book_author, book_id, shelf_num))

print(books[69].book_id)
