# importing modules for abstract base class 
from abc import ABC, abstractmethod


# creating a class for patron
class Patron(ABC):
    
    # constructor to create attributes for patron
    def __init__(self, name, patron_id):
        self.name = name 
        self.patron_id = patron_id
        self.borrowed_books = []
