# Library Management System

This is a Python-based Library Management System that allows users to manage books, users, borrowing and returning of books, and more. The system is designed to help a library manage its operations effectively, including maintaining transaction logs and handling fines for overdue books.

## Features

1. **Book Management**
   - Add books to the library.
   - Remove books from the library.
   - Display details of all books in the library.
  
2. **User Management**
   - Add users with roles (Admin/Regular).
   - Display user details, including borrowed books and fines.

3. **Borrowing and Returning Books**
   - Users can borrow books if available.
   - Users can return books and incur fines for overdue books (1 unit per day overdue).
   - Books can be reserved if all copies are borrowed.

4. **Transaction Logs**
   - Maintain a log of all transactions (borrowing and returning of books).

5. **Fine Management**
   - Charge fines for overdue books.

6. **Reservation System**
   - Allow users to reserve books that are currently borrowed.

## Project Structure

- `LibraryManagment.py`: Contains the `Library` class that manages the library's operations.
- `UserManagment.py`: Contains the `LibraryUser` class that handles user-related functionalities such as borrowing and returning books.
- `main.py`: The main script that demonstrates the usage of the library and user management system.

## Requirements

- Python 3.x
- `datetime` module (standard Python library)

## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/AbdGhazall/PythonProject.git>
   cd <PythonProject>
2. **Run the Project**
   ```bash
   python main.py
