#Practice 00P

class Books:
    def __init__(self, book_ID, author, genre, availability_status):
        self.book_ID = book_ID
        self.author = author
        self.genre = genre
        self.availability_status = availability_status
        
    def display_book_details(self):
        print ("Displaying Book Details")
        print ("_________________________________")
        print (f"Book ID: {self.book_ID}")
        print (f"Author: {self.author}")
        print (f"Genre: {self.genre}")
        print (f"Available books: {self.availability_status}")
        
    def availability_status(self):
        pass
    
class Library():
    def __init__ (self):
        self.books= []
        
    def add_books(self, book):
        self.books.append(book)
        print ("Book added successfully!")
    
    def display_all_books(self):
        print ("All Books in the Library: ")
        for book in self.books:
            book.display_book_details()
    
    def search_book(self, book_ID):
        for book in self.books:
            if book.book_ID == book_ID:
                return book
        return None
    
    def borrow_book(self, book_ID):
        book = self.search_book(book_ID)
        if book:
            if book.availability_status > 0:
                book.availability_status -= 1
                print ("Book borrowed successfully!")
            else: 
                print ("Sorry, the book is currently unavailable.")
        else: 
            print ("Book not found...")
            
    def return_book(self, book_ID):
        book = self.search_book(book_ID)
        if book: 
            book.availability_status += 1
            print ("Book returned successfully!")
        else:
            print ("Book not found...")
  
class User:
    def __init__ (self):
        self.users = {}
            
    def user_registration(self, name, password):
        if name not in self.users:
            self.users[name] = {"password" : password, "borrowed_books" : []}
            print ("Successfully Registered!")
        else:
            print ("Username already taken, try another one")
    
    def user_login(self, name, password, library):
        if name in self.users:
            if password == self.users[name]["password"]:
                print (f"Successfully loged in {name}!")
                sub_main(library, name)
            elif password != self.users[name]["password"]:
                print ("Invalid password, try again!")
        else:
            print (f"Username: {name} not found, try again")
            
                     
def main():
    library = Library()
    users = User()
    while True: 
        print ("\nWELCOME TO THE LIBRARY MANAGEMENT SYSTEM\n")
        print ("1. User Registration")
        print ("2. User Login")
        print ("3. Exit ")
    
        try: 
            choice = int(input("Enter choice: "))
            if choice == 1:
                name = input("Enter username: ")
                password = input("Enter password: ")
                users.user_registration(name, password)
            elif choice == 2:
                name = input("Enter username: ")
                password = input ("Enter password: ")
                users.user_login(name, password, library)
            elif choice == 3:
                print ("\nExiting Program...")
                break
            else:
                print ("Invalid Input, try again")
        except ValueError as e:
            print (f"Error occured: {e}")
            

def sub_main(library, name):
    print ("WELCOME TO THE LIBRARY!")
    print ("1. Display All Books")
    print ("2. Search Books")
    print ("3. Add Book")
    print ("4. Borrow Books")
    print ("5. Return Book")
    print ("6. Return to Main Menu")
    while True:
        try: 
            choice = int(input("Enter choice: "))
            if choice == 1:
                library.display_all_books()
            elif choice == 2:
                book_ID = input("Enter Book ID to search: ")
                book = library.search_book(book_ID)
                library.search_book()
                if book:
                    book.display_book_details()
            elif choice == 3:
                book = input ("Enter book to be added: ")
                library.add_books(book)
            elif choice == 4:
                library.borrow_book(book_ID)
            elif choice == 5:
                library.return_book(book_ID)
            elif choice == 6:
                main()
        except ValueError as e:
            print (f"Error occured: {e}")
            
if __name__ == "__main__":
    main() 
