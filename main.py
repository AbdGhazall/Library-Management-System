from datetime import datetime, timedelta
from LibraryManagment import Library
from UserManagment import LibraryUser

# Create an object from the Library class (instance of the Library)
library = Library()

# Adding two books by sending books title,author,isbn,copies to the add_book method in Library class
library.add_book("The Godfather", "Francis Ford Coppola", "1234590", 2)
library.add_book("Shutter Island", "Martin Scorsese", "1234591", 1)

# Create two users by initializing two objects from LibraryUser class
Abdullrahman = LibraryUser("Abdullrahman", "Admin")
Yazan = LibraryUser("Yazan", "Regular")

# Add the users we made to the library and specifing which type of users
library.add_user("Abdullrahman", "Admin")
library.add_user("Yazan", "Regular")

# now let's let the first user to borrow a one book and the second user borrow two books
# here yazan will be added to the reservation list
library.borrow_book(Abdullrahman, "The Godfather")
library.borrow_book(Yazan, "Shutter Island")
library.borrow_book(Yazan, "The Godfather")

# second user 'yazam' reserve about the book
Yazan.reserve_book("The Godfather", library)

# now displays all books
print("\nBooks in the Library:")
library.display_books()

# displays all users with details
print("\nUsers in the Library:")
library.display_users()

# Example on returning a book with an overdue fine for 20 days
return_date = datetime.now() + timedelta(days=20)
Abdullrahman.return_book("The Godfather", return_date, library)

# Display all books and all users after returning the borrowed books
print("\nBooks in the Library After Return:")
library.display_books()
print("\nUsers in the Library After Return:")
library.display_users()

# Display transaction logs if any made
library.display_transactions()

# let's say 'abdullrahman' pays only a part of the fine at first. then he payed the rest of it
Abdullrahman.pay_fine(5)
Abdullrahman.pay_fine(1)

# now we can show the user's details after pay the fines for the borrowed books
print("\nUsers in the Library After Paying Fines:")
library.display_users()