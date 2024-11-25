DATABASE_FILE = "./database/books.txt"
import os


def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """

    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "a") as f:
            f.write("")


def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    with open(DATABASE_FILE, "a") as f:
        f.write(f"{title},{author}")


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    book = {}
    with open(DATABASE_FILE, "r") as f:
        book = f.readlines()


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
