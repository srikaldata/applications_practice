# 


class Book:
    def __init__(self, name, price, isbn, pages):
        self.name = name
        self.price = price
        self.isbn = isbn
        self.pages = pages
        self.is_available = True
        

readers_digest_mag = Book(name = "Reader's Digest", price = 30, isbn = '1A2B3C', pages = 50)
overdrive_mag  = Book(name = "Overdrive", price = 25, isbn = '1Z2Y3X', pages = 40)

print(readers_digest_mag.name)
print(overdrive_mag.isbn)

readers_digest_mag.contest = 'Crossword'
print(readers_digest_mag.contest)

# a member should not change the name of the book and create a new name (fake identity)