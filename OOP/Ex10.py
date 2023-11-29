# Description:
# Develop a Library Management System that includes multiple classes and relationships to represent the various entities within a library. It should include:
#
# Book Class: Holds details about individual books, including title, author, ISBN, availability status, etc.
#
# User Class: Represents library users (members) with information like name, member ID, current checkouts, etc.
#
# Librarian Class: A subclass of the user with additional privileges such as adding books, managing users, etc.
#
# Transaction Class: Represents a transaction in the library, such as checking out or returning a book. Includes details about the user, book, transaction type, date, etc.
#
# Library Class: The main class that combines all the others, containing lists of books, users, and librarians. It should have methods to perform various library tasks like searching books, checking out books, returning books, managing users, etc.
from datetime import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

class User:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.current_checkouts = []
        self.banned = False

    def checkout_book(self, book):
        if self.banned:
            return "You are banned and cannot check out books"
        if book.availability_status:
            self.current_checkouts.append(book)
            book.availability_status = False
            return f"Book {book.title} has been checked out"
        else:
            return f"Book {book.title} is not available. Try reaching out to a librarian to see if it can get ordered."

    def return_book(self, book):
        if book in self.current_checkouts:
            self.current_checkouts.remove(book)
            book.availability_status = True
            return f"Book {book.title} has been returned"
        else:
            return f"You have not checked out this book: {book.title}"

class Librarian(User):
    def add_book(self, library, book):
        library.books.append(book)
        return f"Book {book.title} added to the library."

    def ban_user(self, user):
        user.banned = True
        return f"User {user.name} has been banned"

class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type
        self.date = datetime.now()

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.librarians = []
        self.transactions = []

    def search_book(self, title):
        found_books = []
        for book in self.books:
            found_books.append(book)
        return found_books

    def checkout_book(self, user, book):
        if user in self.users:
            return user.checkout_book(book)
        else:
            return "User not found"

    def return_book(self, user, book):
        if user in self.users:
            return user.return_book(book)
        else:
            return "User not found"
