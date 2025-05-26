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

    # method to return book 
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
    
    # display the info of the patron
    def display_info(self):
        print(f'{self.name} (ID: {self.patron_id}) - Borrowed books: {[b.title for b in self.borrowed_books]}')


# inheriting Patron (parent) class within Student (child) class  
class Student(Patron):
    
    # making the abstract method concrete post inheritance
    def max_books_allowed(self):
        return 3

