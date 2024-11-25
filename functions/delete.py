DATABASE_FILE = "./database/books.txt"

with open(DATABASE_FILE, "r") as f:
    book = f.readlines()
print(book)
