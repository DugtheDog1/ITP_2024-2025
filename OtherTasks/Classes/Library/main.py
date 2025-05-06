

class Book:
    def __init__(self, title, author, in_section, in_isle):
        self.title = title
        self.author = author
        self.in_section = in_section
        self.in_isle = in_isle

class Library:
    def __init__(self):
        self.books = []

    def list_books(self, books):
        return len(books)

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id






