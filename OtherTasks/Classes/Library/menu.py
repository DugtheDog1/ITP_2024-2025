import json

def show_books():
    current_books = []  # Keep current_books local to the function to avoid global side effects
    with open("OtherTasks/Classes/Library/books.json", "r") as x:
        data = json.load(x)
        # Make sure "books" is in data, then iterate through the list of books
        for book in data.get("books", []):
            # Check if the book object has a title
            if "title" in book:
                current_books.append(book["title"])
    print(current_books)

show_books()
