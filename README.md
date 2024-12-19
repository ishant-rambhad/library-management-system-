# Library Management System

## Project Overview

The Library Management System is a simple web application designed to manage the day-to-day operations of a library. It allows library administrators to efficiently manage books and members by providing features to add, edit, delete, and view records of books and members.

This project is built using **Flask**, a lightweight Python framework for web development, and **SQLite** as the database for storing data. The application uses **SQLAlchemy** for database interaction, and **Bootstrap** is used for creating a responsive design.

## Features

- **Manage Books**: Admin can view, add, edit, or delete books in the library.
- **Manage Members**: Admin can view, add, edit, or delete members.
- **Responsive Design**: The application is designed with a mobile-first approach, making it responsive across various screen sizes.

## Technologies Used

- **Flask**: Web framework for Python.
- **SQLite**: A lightweight relational database management system.
- **SQLAlchemy**: ORM (Object-Relational Mapping) for database operations.
- **Bootstrap**: Frontend framework for responsive design.

## Project Structure
/library-management-system
│
├── app.py                    # Main application file with routes and logic
├── library.db                # SQLite database file
├── requirements.txt          # File listing project dependencies
│
├── templates/                # Folder containing HTML templates for rendering pages
│   ├── index.html            # Home page template
│   ├── books.html            # Page displaying list of books
│   ├── add_book.html         # Template for adding new book
│   ├── edit_book.html        # Template for editing book details
│   ├── members.html          # Page displaying list of members
│   ├── add_member.html       # Template for adding new member
│   ├── edit_member.html      # Template for editing member details
│
└── static/                   # Folder containing static files like CSS, JS, and images
    ├── css/                  # Folder for CSS files
    │   └── styles.css        # Custom styles for the application
    ├── js/                   # Folder for JS files (if needed in the future)
    └── images/               # Folder for image files (if any)


### Key Components

- **`Book` Model**: Represents the `books` table in the database with fields for `id`, `title`, `author`, and `year`.
- **`Member` Model**: Represents the `members` table with fields for `id`, `name`, and `email`.

### Routes

- **Home Page (`/`)**: Renders the index page.
- **Books Routes**:
  - **`/books`**: Displays a list of all books in the library.
  - **`/add_book`**: Displays a form for adding a new book.
  - **`/edit_book/<id>`**: Displays a form to edit the details of an existing book.
  - **`/delete_book/<id>`**: Deletes a book from the library.
- **Members Routes**:
  - **`/members`**: Displays a list of all members in the library.
  - **`/add_member`**: Displays a form for adding a new member.
  - **`/edit_member/<id>`**: Displays a form to edit the details of an existing member.
  - **`/delete_member/<id>`**: Deletes a member from the library.

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system


2. Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```

3. Run the application:

```bash
Copy code
python app.py
```
4. The application will be running at http://127.0.0.1:5000/ on your local machine.


