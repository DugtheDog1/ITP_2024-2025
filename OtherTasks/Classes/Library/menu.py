import json

with open("OtherTasks/Classes/Library/books.json", "r") as x:
    data = json.load(x)
    for book in data["books"]:
        print(book["title"])
