from random import randint
from models import Book


books = []

for x in range(100):
    book_title = f"Book Title {x}"
    book_author = f"Book Author {x}"
    book_id = randint(1, 12000)
    isle_num = randint(1, 15)
    shelf_num = randint(1, 5)
    books.append(Book(book_title, book_author, book_id, isle_num, shelf_num))


with open("OtherTasks/Classes/Library/my_list.txt", "w") as x:
    for book in books:
        x.write(f"{book.title}, {book.author}, {book.id}, {isle_num}, {shelf_num} \n")

print("List saved to my_list.txt")