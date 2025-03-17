# QuickDBAPP - User Management System with FastAPI

QuickDBAPP is a **User Management System** built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This application provides basic **CRUD** (Create, Read, Update, Delete) operations for managing users. The frontend is built using **HTML**.

## Features

- **Add User**: Add a new user to the system.
- **View Users**: View a list of all users in the database.
- **Update User**: Edit the user details (name, email).
- **Delete User**: Remove a user from the database.
- **Frontend**: Basic HTML frontend with forms and user management features.

## Tech Stack

- **Backend**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML
- **Static Files**: CSS

## Setup

Follow these steps to set up **QuickDBAPP** locally.

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/QuickDBAPP.git
cd QuickDBAPP
```

### 2. Create a Virtual Environment

It’s recommended to use a virtual environment for Python dependencies:

```bash
python -m venv env
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

After setting up the virtual environment and installing the dependencies, you can start the FastAPI server:

```bash
uvicorn mainapp.main:app --reload
```

The app will run on [http://127.0.0.1:8000](http://127.0.0.1:8000). You can access the frontend at this URL and perform CRUD operations on users.

### 5. Access the Documentation

FastAPI automatically generates documentation for the API. You can access it at:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc UI](http://127.0.0.1:8000/redoc)

### 6. Create the Database

The database is automatically created upon starting the application. The `User` table is created in an SQLite database (`database.db`) to store user details. You can find this file in the project directory.

## Project Structure

```
QuickDBAPP/
├── env/                # Virtual environment
├── mainapp/            # Main application code
│   ├── __init__.py     # Init file for the app
│   ├── database.py     # Database connection and session management
│   ├── main.py         # FastAPI app and routes
│   ├── models.py       # SQLAlchemy models for the database
│   ├── schemas.py      # Pydantic schemas for data validation
│   ├── static/         # Static files (e.g., CSS)
│   ├── templates/      # HTML templates
│   └── database.db     # SQLite database file
└── requirements.txt    # Project dependencies
```
