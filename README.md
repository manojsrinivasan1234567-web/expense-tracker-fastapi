# 💰 Expense Tracker API

A RESTful Expense Tracker API built using **Python, FastAPI, and PostgreSQL** to manage daily expenses through CRUD operations.

## 📌 Project Overview

The Expense Tracker API helps users record, retrieve, update, and delete expense details. It uses PostgreSQL to store expense records and FastAPI to provide REST API endpoints.

## 🚀 Features

- Create new expense records
- Retrieve all expenses
- Retrieve an expense by ID
- Update existing expenses
- Delete expenses
- Calculate total expenses
- Validate request data
- Store data in PostgreSQL
- Interactive API documentation using Swagger UI

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **ASGI Server:** Uvicorn
- **Environment Configuration:** python-dotenv
- **API Testing:** Swagger UI

## 📂 Project Structure

```text
expense_tracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── .env
├── .gitignore
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker-fastapi.git
cd expense-tracker-fastapi
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named `expense_db`.

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/expense_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

**Security:** Never upload `.env` or expose database passwords in GitHub.

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload
```

## 📖 API Documentation

Once the server is running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **API Home:** http://127.0.0.1:8000/

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | Get all expenses |
| GET | `/expenses/summary` | Get total spending |
| GET | `/expenses/{expense_id}` | Get an expense by ID |
| PATCH | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## 🧪 Sample Request

Create an expense using `POST /expenses`:

```json
{
  "title": "Grocery Shopping",
  "amount": 850,
  "category": "Food",
  "expense_date": "2026-10-15",
  "description": "Weekly groceries"
}
```

## 🎯 Learning Outcomes

- Building REST APIs with FastAPI
- Implementing CRUD operations
- Connecting Python applications to PostgreSQL
- Using SQLAlchemy for database operations
- Validating API requests using Pydantic
- Testing endpoints through Swagger UI
- Managing Python project dependencies and configuration

## 🔮 Future Enhancements

- User registration and login
- JWT authentication and password hashing
- User-specific expense management
- Monthly and category-wise expense reports
- Frontend dashboard and data visualization


---

⭐ If you find this project useful, feel free to star the repository.
