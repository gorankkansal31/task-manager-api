⭐ Task Manager API – Django REST Framework

A complete Task Manager REST API built using Django REST Framework.
This API supports:

User registration & login using JWT

Task creation, updating, deletion (CRUD)

Pagination (5 tasks per page)

Filtering tasks by completion

Owner-based permissions (only owner can modify tasks)

Admin users can view all tasks

Swagger API documentation

Unit tests for API validation

This project is structured for clean maintainability and follows standard backend development practices.

🧩 1. Project Overview

This Task Manager API allows authenticated users to manage tasks.
Each user can:

Create tasks

View their own tasks

Update their own tasks

Delete their own tasks

Admin users can view all tasks globally.

JWT tokens ensure secure, token-based authentication.

⚙️ 2. Setup Instructions (No Clone Required)

Follow these steps to run the project locally.

✔ Step A: Activate Virtual Environment

(Use your existing environment)

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

✔ Step B: Install Dependencies

Use the included requirements.txt:

pip install -r requirements.txt

✔ Step C: Apply Migrations
python manage.py migrate

✔ Step D: Start the Server
python manage.py runserver


Server runs on:
👉 http://127.0.0.1:8000/

📌 3. API Endpoints
🔐 Authentication (JWT)
Method	Endpoint	Description
POST	/auth/register/	Register a new user
POST	/auth/token/	Login (returns access & refresh tokens)
POST	/auth/token/refresh/	Refresh access token
📝 Task Endpoints (CRUD)
Method	Endpoint	Description
GET	/tasks/	List all tasks (paginated & filtered)
POST	/tasks/	Create a new task
GET	/tasks/<id>/	Retrieve single task
PUT	/tasks/<id>/	Update task
DELETE	/tasks/<id>/	Delete task
🔍 4. Pagination & Filtering
✔ Pagination

Each page contains 5 tasks:

/tasks/?page=1

✔ Filter Tasks by Status

Completed tasks:

/tasks/?completed=true


Pending tasks:

/tasks/?completed=false

📘 5. API Documentation (Swagger)

Interactive documentation available at:

👉 Swagger UI:
http://127.0.0.1:8000/swagger/

👉 ReDoc UI:
http://127.0.0.1:8000/redoc/

Includes:

All API routes

Request/response schemas

Live testing environment

🔐 6. Permissions & Roles
👤 Normal User

Can create tasks

Can view only their own tasks

Can update/delete only their tasks

🛠 Admin User

Can view ALL tasks

Has access to admin panel

Can manage all records

This is enforced using custom permissions.

🧪 7. Running Tests

Run complete test suite:

python manage.py test


Expected output:

Ran X tests in Y seconds
OK


This validates:

API behavior

CRUD correctness

Authentication

Permissions

🧱 8. Project Structure
task-manager-api/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── tests/
│   └── migrations/
│
├── requirements.txt
├── manage.py
└── .gitignore


The project follows clean modular architecture.

🛠 9. Tech Stack

Python 3

Django

Django REST Framework

SimpleJWT

SQLite

Swagger (drf-yasg)

👤 10. Author

Gorank Kansal
Backend Developer — Task Manager API Assignment




