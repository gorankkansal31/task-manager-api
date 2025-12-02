# 📝 Task Manager API – Django REST Framework

A fully functional RESTful API for managing tasks, built using **Django REST Framework**.  
This project supports CRUD operations, JWT authentication, pagination, filtering, user roles,  
and complete API documentation using Swagger.

---

## ⭐ 1. Project Description

This API allows users to:

- Register & Login (JWT authentication)
- Create, view, update & delete tasks
- View ONLY their own tasks (except admin)
- Filter tasks by completion status
- Use paginated task lists (5 per page)
- Access interactive API docs via Swagger & ReDoc

---

## 🚀 2. Setup & Run Instructions

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/gorankkansal31/task-manager-api.git
cd task-manager-api

Step 2: Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

🔹 Step 3: Install Dependencies
pip install -r requirements.txt

🔹 Step 4: Run Migrations
python manage.py migrate

🔹 Step 5: Start Development Server
python manage.py runserver


API will be available at:
👉 http://127.0.0.1:8000/

📌 3. API Endpoints
🔐 Authentication Endpoints
Method	Endpoint	Description
POST	/auth/register/	Register new user
POST	/auth/token/	Login (JWT Access + Refresh token)
POST	/auth/token/refresh/	Refresh access token
🗂 Task Management Endpoints
Method	Endpoint	Description
GET	/tasks/	List all tasks (pagination + filters)
POST	/tasks/	Create new task
GET	/tasks/<id>/	Retrieve task
PUT	/tasks/<id>/	Update task
DELETE	/tasks/<id>/	Delete task
🔍 4. Filters & Pagination
✔ Pagination

Each page returns 5 tasks
Example:

/tasks/?page=2

✔ Filtering

Filter by completed status:

/tasks/?completed=true
/tasks/?completed=false

📘 5. Swagger API Documentation

Interactive documentation is available at:

👉 Swagger UI: http://127.0.0.1:8000/swagger/



It includes:

All API endpoints

Request & Response schemas

Live API testing

🧪 6. Running Tests

Run all unit tests:

python manage.py test


If successful:

Ran X tests in Y seconds
OK

👥 7. User Roles (Bonus)

Admin users → Can view ALL tasks

Normal users → Can view/update/delete ONLY their own tasks

Enforced using custom permissions

⭐ 8. Tech Stack

Python 3.12

Django

Django REST Framework

SimpleJWT

SQLite

Swagger (drf-yasg)
