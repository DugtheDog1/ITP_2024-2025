

class Book:
    def __init__(self, title, author, book_id, isle, shelf):
        self.title = title
        self.author = author
        self.id = book_id
        self.isle = isle
        self.shelf = shelf

class Library:
    def __init__(self):
        self.books = []

    def list_books(self, books):
        return len(books)

class User:
    def __init__(self):  
        self.name = None
        self.password = None

    def new_user(self, name, password):
        self.name = name
        self.password = password








