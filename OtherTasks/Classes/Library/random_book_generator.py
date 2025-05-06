from random import randint
from models import Book
import json

books = []

def generate_books():
    for x in range(100):
        book_title = f"Book Title {x}"
        book_author = f"Book Author {x}"
        id = randint(1, 12000)
        isle = randint(1, 15)
        shelf = randint(1, 5)
        books.append(Book(book_title, book_author, id, isle, shelf))

def save_books():
    with open("OtherTasks/Classes/Library/books.json", "w") as x:
        book_dict = [{"title": book.title, "author": book.author, "id": book.id, "isle": book.isle, "shelf": book.shelf} for book in books]
        json.dump({"books": book_dict}, x, indent=4)



generate_books()
save_books()
