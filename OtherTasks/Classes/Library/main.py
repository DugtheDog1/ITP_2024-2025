

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



books = [
    Book("To Kill a Mockingbird", "Harper Lee", "1", "3"),
    Book("1984", "George Orwell", "2", "2"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "3", "3")
]


print(Library().list_books(books))

