

def show_menu():
    print("""
          --- Welcome to the Library ---
          Enter the nubmer
          * enter 1 -> to Add book
          * enter 2 -> to Add member
          * enter 3 -> to Issue book
          * enter 4 -> to Return book
          * enter 5 -> to Show members
          * enter 6 -> to Show books
          * enter 7 -> to Exit
          """)

while True:
    show_menu()
    choice = input('Choose: ')
    
    if choice == '1':
        t = input('Title: ')
        a = input('Author: ')
        i = input('ISBN: ')
        library.add_book(t, a, i)
        
    elif choice == '2':
        