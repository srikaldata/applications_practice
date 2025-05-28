# importing the classes
from book import Book
from patron import Student, Faculty

# aggregate class --> Library is a wrapper for other functions
class Library:
    # constructor method to create a book shelf and current patrons list
    def __init__(self):
        self.books_shelf = []
        self.patrons_current = []
        
    # method to add book to the library shelf
    def add_book(self, title, author, isbn):
        self.books_shelf.append(Book(title, author, isbn))
       
    # method to add patron 
    def add_patron(self, name, patron_id, patron_type='student'):
        if patron_type == 'faculty':
            self.patrons_current.append(Faculty(name, patron_id))
        elif patron_type == 'student':
            self.patrons_current.append(Student(name, patron_id))
        
    # method to find the name of the book when isbn is given
    def find_book(self, isbn):
        return next((b for b in self.books_shelf if b.isbn == isbn))
    
    # method to find the patron in the library
    def find_patron(self, patron_id):
        return next((p for p in self.patrons_current if p.patron_id == patron_id))
    
    # method to issue the book 
    def issue_book(self, patron_id, isbn):
        book = self.find_book(isbn)
        patron = self.find_patron(patron_id)
        if book and patron:
            return patron.borrow_book()
