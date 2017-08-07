class Book:
    """A simple class to initialise a book"""

    def __init__(self, name, author, price):

        self._name = name
        self._author = author
        self._price = price

    def get_details(self):

        return self._name, self._author, self._price

class Library:

    def __init__(self):

        self._books = []

    def add_to_library(self, book):

        self._books.append(book)

    def view_books(self):

        for each_book in self._books:
            print (each_book.get_details())

if __name__ == '__main__':

    book_one = Book('Data Structures and Algorithms in Python', 'Gaurav Singh', 400)
    my_library = Library()
    my_library.add_to_library(book_one)
    book_two = Book('Python Manual', 'Gaurav Singh', 125)
    my_library.add_to_library(book_two)
    my_library.view_books()
