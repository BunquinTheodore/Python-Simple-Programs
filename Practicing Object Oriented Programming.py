#Practicing Object Oriented Programming

class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
        
    def display_details(self):
        print ("Book Details")
        print (f"Title: {self.title}")
        print (f"Author: {self.author}")
        print (f"ISBN: {self.isbn}")
        print (f"Available Copies: {self.available_copies}")
    
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print ("Book checked out successfully!")
        else:
            print ("Available copies of this book is insufficient")
    
    def return_book(self):
        self.available_copies += 1
        print ("Book returned successfully!")
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print (f"The book {book} is removed from the library")
        else:
            print (f"The book {book} is not in the library")
    
    def search_book(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                book.display_details()
    
    def total_books(self):
        print (f"Total Books in the Library: {len(self.books)}")

def main():
    library = Library()
    print ("Welcome to the Library!\n")
    print ("1. Add Book")
    print ("2. Remove Book")
    print ("3. Return Book")
    print ("4. Borrow Book")
    print ("5. Search Book")
    print ("6. Total Books")
    print ("7. Exit")
    while True: 
        try: 
            choice = int(input("Enter choice: "))
            if choice == 1:
                Library.add_book()
            elif choice == 2:
                Library.remove_book()
            elif choice == 3:
                Book.return_book()
            elif choice == 4:
                Book.check_out()
            elif choice == 5:
                Library.search_book()
            elif choice == 6:
                Library.total_books()
            elif choice == 7: 
                print ("Exiting Program...")
                break
            else:
                print ("Invalid Input")
        except ValueError as e:
            print (f"Error: {e}")
            
        
        
if __name__ == "__main__":
    main() 
    
