from UserManagment import LibraryUser
from datetime import datetime

#class Library contaians all methods needed to the Library managment
class Library:
    def __init__(self):
        self.books = [] #empty list to store the books
        self.users = [] #empty list for users details
        self.transactions = []  #empty list to store transaction logs
    
    #This method adds the book details to store it into the books list as a dictionary (key and value) 
    def add_book(self, title, author, isbn, copies):
        book = {'title': title, 'author': author, 'isbn': isbn, 'copies': copies, 'reservations': []}
        self.books.append(book)
        print(f"'{title}' added to the library with {copies} copies.")

    #This method remove books from the library
    '''
        First, it checks if the book is already in the library (the list) then, it remove the book from the list if exist.
        if book name is not in the library (list) it shows "not found" message.
    '''
    def remove_book(self, title):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"'{title}' Was removed from the library.")
        else:
            print(f"Book '{title}' not found.")

    #This method to display and show all books details
    '''
        Display all books details by calling the key for each attribute,
        if the book doesn't exist in the books list it shows a "no books" message.
    '''
    def display_books(self):
        if not self.books:
            print("There are no books in the library.")
            return
        for book in self.books:
            reservations = [user.name for user in book['reservations']]
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Copies: {book['copies']}, Reservations: {reservations}")

    #This method adds the users details
    '''
        It should take 2 arguments name and role, If role was anything else it shows "invalid" message.
        here we create an object from the class LibraryUser, and add the user details after calling to the users list.
    '''
    def add_user(self, name, role='Regular'):
        if role not in ['Admin', 'Regular']:
            print("Invalid role. Please choose whether you're 'Admin' or 'Regular'.")
            return
        user = LibraryUser(name, role)
        self.users.append(user)
        print(f"User '{name}' added with role '{role}'.")

    #This method to display all users details username, role, borrowed books and fines
    '''
        Firts it checks if the user is exist in the users list or not,
        Then it retrives all user details and user fines would be shown as 2 decimal places.
    '''
    def display_users(self):
        if not self.users:
            print("No users in the library yet.")
            return
        for user in self.users:
            print(f"Username: {user.name}, Role: {user.role}, Borrowed Books: {list(user.borrowed_books.keys())}, Fines: ${user.fines:.2f}")

    #simple method to search and find the book by checking the book title
    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None
    
    #This method to manga borrow books process
    '''
        First, it try to locate the book and check about the book availability.
        If book is available it updates the number of book's copies.
        If there are no copies so it add the user to the reservation list.
    '''
    def borrow_book(self, user, title):
        book = self.find_book(title)
        if book:
            if book['copies'] > 0:
                book['copies'] -= 1
                user.borrow_book(title, datetime.now())
                print(f"{user.name} borrowed '{title}'.")
            else:
                print(f"No copies of '{title}' available. Adding {user.name} to reservation list.")
                book['reservations'].append(user)
        else:
            print(f"Book '{title}' not found.")
    
    #This method to manage return books process
    '''
        First, it checks if the book exist or not. Then it updates the number of copies for each book.
        it also handle reservations by checking if there are any users waiting for the book. then it notifies the first user in the reservation list.
    '''
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book['copies'] += 1
            if book['reservations']:
                next_user = book['reservations'].pop(0)
                print(f"'{title}' is available now. Notifying {next_user.name}.")
                self.borrow_book(next_user, title)

    #This method creates a timestamp of the current date and time and This log entry is then added to a list of transactions
    def log_transaction(self, user, book_title, transaction_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if user:
            log_entry = f"{timestamp} - {user.name} ({user.role}) {transaction_type} '{book_title}'"
        else:
            log_entry = f"{timestamp} - Book '{book_title}' was returned and made available"
        self.transactions.append(log_entry)

    #Dispaly and show all transaction logged if any
    def display_transactions(self):
        if not self.transactions:
            print("No transactions logged.")
            return
        print("\nTransaction Logs:")
        for transaction in self.transactions:
            print(transaction)

    #This method manages the reservation of a book
    '''
        First, it check the availability of the book, if it is available user can borrow it
        if book isn't available then method adds the user to the reservation list
    '''
    def reserve_book(self, user, title):
        book = self.find_book(title)
        if book:
            if book['copies'] > 0:
                print(f"Book '{title}' is available. No need for reservation.")
                self.borrow_book(user, title)
            else:
                if user not in book['reservations']:
                    book['reservations'].append(user)
                    print(f"{user.name} reserved '{title}'.")
                else:
                    print(f"{user.name} has already reserved '{title}'.")
        else:
            print(f"Book '{title}' not found.")