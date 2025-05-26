
# creating a class for the basic unit of library - a book
class Book:
    
    # constructor function with the details of the book
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
        
    # method to check availability and borrow the book    
    def borrow_book(self, patron_id):
        if self.available:
            self.available = False
            self.borrower = patron_id
            return True
        return False
    
    # method to return the book and make the book available
    def return_book(self):
        self.available = True
        self.borrower = None
    
    # dunder / magic method for printing the object     
    def __str__(self):
        status = 'Available' if self.available else f'Borrowed by {self.borrower}'
        return f'{self.title} by {self.author} | ISBN: {self.isbn} | {status}' 
    
