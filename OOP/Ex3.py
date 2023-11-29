# 3. Задача: Създайте клас за управление на библиотека, който инкапсулира списъка с книги и позволява търсене и заемане само на
# регистрирани потребители.
# Вход: потребител "Alice", заема книга "Python Basics"
# Изход: статус на заемането

class ManageLibrary:
    def __init__(self):
        self.__books = {}
        self.__users = {}

    def add_book(self, book_title):
        self.__books[book_title] = True

    def register_user(self, name):
        self.__users[name] = []

    def checkout_book(self, name, book_title):
        if name in self.__users and book_title in self.__books and self.__books[book_title]:
            self.__users[name].append(book_title)
            self.__books[book_title] = False
            return f"{name} checked out the book {book_title}"
        elif name not in self.__users:
            return f"{name} is not registered. Please register first."
        elif book_title not in self.__books:
            return f"{book_title} is not available"

    def return_book(self, name, book_title):
        if name in self.__users and book_title in self.__users[name]:
            self.__users[name].remove(book_title)
            self.__books[book_title] = True
            return f"{name} returned book {book_title}"
        elif name not in self.__users:
            return f"{name} is not registered. Please register first."
        elif book_title not in self.__users[name]:
            return f"{name} has not checked out this book {book_title}"
        else:
            return f"{book_title} is not available in the library"

example = ManageLibrary()
example.add_book("Book 1")
example.add_book("Book 2")

example.register_user("Pesho")

takebook = example.checkout_book("Pesho", "Book 1")
print(takebook)