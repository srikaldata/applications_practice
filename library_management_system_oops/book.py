
# creating a class for the basic unit of library - a book
class Book:
    
    # constructor function with the details of the book
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
