# importing the classes
from book import Book
from patron import Student, Faculty

# aggregate class --> Library is a wrapper for other functions
class Library:
    # constructor method to create a book shelf and current patrons list
    def __init__(self):
        self.books_shelf = []
        self.patrons_current = []
