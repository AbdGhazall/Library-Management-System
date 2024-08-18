from datetime import datetime
class LibraryUser:
    def __init__(self, name, role='Regular'):
        self.name = name
        self.role = role  # to specify wether the user is Admin or Regular
        self.borrowed_books = {} # a dictionary to store all borrowed books details 
        self.fines = 0.0  # making fines starts from 0 as a default value

    # Method to borrow a book by send the argument book title
    def borrow_book(self, book_title, borrow_date):
        self.borrowed_books[book_title] = borrow_date

    # Method to return a book process
    '''
        It calculates if the book is returned late or computes any applicable fine, and updates the user’s fines,
        It also notifies the library that the book has been returned and updates the library’s records.
        here we have assumed that 14 day is the borrowing deadline, and $1 per overdue day.
    '''
    def return_book(self, book_title, return_date, library):
        if book_title in self.borrowed_books:
            borrow_date = self.borrowed_books.pop(book_title)
            days_borrowed = (return_date - borrow_date).days
            if days_borrowed > 14:
                overdue_days = days_borrowed - 14
                fine = overdue_days * 1.0
                self.fines += fine
                print(f"{self.name} returned '{book_title}' late. Fine: ${fine:.2f}.")
            else:
                print(f"{self.name} returned '{book_title}' on time.")
            library.return_book(book_title)
        else:
            print(f"{self.name} did not borrow '{book_title}'.")

    #method to handle user's fines so they can pay any fines
    '''
        it first check that the amount needed to be payed no exceed the user total fines
        then user can pay some of the fines not all of them and show to the user the left fines.
    '''
    def pay_fine(self, amount):
        if amount <= self.fines:
            self.fines -= amount
            print(f"{self.name} paid ${amount:.2f}. Remaining fines: ${self.fines:.2f}.")
        else:
            print(f"Amount exceeds the total fines. {self.name} owes ${self.fines:.2f}.")

    #this method calls the reserve_book from the library class to  handle book reservations
    def reserve_book(self, book_title, library):
        library.reserve_book(self, book_title)
