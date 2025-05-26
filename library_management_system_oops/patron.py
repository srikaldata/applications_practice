# importing modules for abstract base class 
from abc import ABC, abstractmethod


# creating a class for patron
class Patron(ABC):
    
    # constructor to create attributes for patron
    def __init__(self, name, patron_id):
        self.name = name 
        self.patron_id = patron_id
        self.borrowed_books = []
        
    # abstraction in parent fn --> must define this fn in the child fn    
    @abstractmethod
    def max_books_allowed(self):
        pass

    # method for borrowing a book
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books_allowed():
            if book.borrow_book(self.patron_id):
                self.borrowed_books.append(book)
                return True
        return False
    