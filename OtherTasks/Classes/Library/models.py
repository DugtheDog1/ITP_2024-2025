

class Book:
    def __init__(self, title, author, id, isle_num, shelf_num):
        self.title = title
        self.author = author
        self.id = id
        self.isle_num = isle_num
        self.shelf_num = shelf_num


class Library:
    def __init__(self):
        self.books = []

    def list_books(self, books):
        return len(books)

class User:
    def __init__(self):  # Correct constructor name
        self.name = None
        self.password = None

    def new_user(self, name, password):  # Correct indentation and method definition
        self.name = name
        self.password = password








