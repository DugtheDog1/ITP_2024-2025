import json



def add_book():
    # new_book_title = input("Enter new book title: ")
    # new_book_author = input("Enter new book author: ")
    # new_book_id = input("Enter new book id: ")
    # new_book_isle = input("Enter new book isle: ")
    # new_book_shelf = input("Enter new book shelf: ")
    with open("OtherTasks/Classes/Library/books.json", "r") as x:
        new_file = json.load(x)
        print(new_file["bonew_book = { "title": new_book_title, "author": new_book_author, "id": new_book_id, "isle": new_book_isle, "shelf": new_book_shelf }
oks"][0]["title"])
# 
add_book()