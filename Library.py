# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 22:14:38 2024

@author: ThomasB
"""
class Library:
    def __init__(self, books_available, books_out, total_users):
        self.books_available = books_available
        self.books_out = {}
        self.total_users = total_users
        
    def check_out_book(self, book_name, user):
        # Iterate over the available books to check if the book is available
        for book in self.books_available:
            print(f"Checking {book.name} against {book_name}")  # Debugging print
            if book.name == book_name:
                self.books_available.remove(book)  # Remove the book from available books
                # Iterate over the users to check if the user is registered
                for people in self.total_users:
                    if people.user_name == user:
                        self.books_out[book] = user  # Add the book to checked out books
                        print('Here is your copy of the book')
                        return
                print('Go get a library card first')
                return
        # If the book wasn't found in the available books, check if it's already checked out
        for book in self.books_out:
            if book.name == book_name:
                print('This book has been checked out already')
                return
        print('This book is not a part of our collection')  # If book doesn't exist in the collection

class Book:
    def __init__(self, name, Author):
        self.name = name
        self.Author = Author
    
    def __hash__(self):
        return hash((self.name, self.Author))  # Hashable by combining the name and author
    
    def __eq__(self, other):
        print(f"Comparing {self} with {other}")  # Debugging print
        return isinstance(other, Book) and self.name == other.name and self.Author == other.Author

class library_user:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        
class Librarian(library_user):
    def __init__(self,user_id,user_name,password):
        super().__init__(user_id,user_name)
        self.password = password
        
    def check_registry(self, password, Library):
        if password == self.password:
            print('Hello Librarian! Here is the registry')
            print(Library.books_available)
        else:
            print('Password is incorrect')
        

book1 = Book('Silence of the Lambs', 'Some Guy')
book2 = Book('Red Rising', 'Another Guy')
user1 = library_user('user1', 'Tommi')
user2 = library_user('user2', 'Leanna')
user3 = library_user('user3', 'Boobi')
librarian = Librarian('superuser', 'baddass', 'L' )

def main():
    books_available = [book1, book2]
    total_users = [user1, user2, user3]
    books_out = {}
    TB_Library = Library(books_available, books_out, total_users)
    
    while True:
        print('Welcome to Thomas Brown Library. Please select an operation')  
        print('Option 1: Check out a book')
        print('Option 2: Exit')
        print('Option 3: Librarian Log In')
        choice = input('Enter an option:')
        choice = int(choice)
        
        if choice == 1:
            user_input = input('Please enter your username and the title of the book you would like to check out, separated by a comma')
            book_name, user = user_input.split(",")
            user = user.strip()
            book_name = book_name.strip()
            TB_Library.check_out_book(book_name, user)
        
        elif choice == 2:
            print('Goodbye')
            break
        elif choice == 3:
            password = input('Please enter your password')
            librarian.check_registry(password, TB_Library)
        else:
            print('No valid input')

if __name__ == "__main__":
    main()
