import json

def add_book():
    new_book_title = input("Enter new book title: ")
    new_book_author = input("Enter new book author: ")
    new_book_id = input("Enter new book id: ")
    new_book_isle = input("Enter new book isle: ")
    new_book_shelf = input("Enter new book shelf: ")

    new_book = {
        "title": new_book_title,
        "author": new_book_author,
        "id": new_book_id,
        "isle": new_book_isle,
        "shelf": new_book_shelf
    }

    file_path = "OtherTasks/Classes/Library/books.json"

    # Read existing data
    with open(file_path, "r") as f:
        books = json.load(f)

    # Append new book
    books.append(new_book)

    # Write back to file
    with open(file_path, "w") as f:
        json.dump(books, f, indent=4)

    print("Book added successfully.")



add_book()
