# 🚀 Task Manager API – Django REST Framework

A complete **Task Manager REST API** that allows authenticated users to manage tasks securely.  
This project includes **JWT Authentication**, CRUD operations, pagination, filtering, Swagger docs, and unit tests.

## 🧱 System Architecture Diagram
```
                   +---------------------------+
                   |     Client / Frontend     |
                   |  (Postman / Browser / UI) |
                   +-------------+-------------+
                                 |
                                 v
                     HTTP Requests (JSON API)
                                 |
                                 v
        +------------------------------------------------+
        |                Django REST API                 |
        |------------------------------------------------|
        |   URLs   |   Views   | Serializers |  Models   |
        +------------------------------------------------+
                                 |
                                 v
                       Business Logic Layer
                                 |
                                 v
        +------------------------------------------------+
        |                Permissions Layer               |
        |  - JWT Authentication                           |
        |  - Owner-based Access                           |
        |  - Admin Privileges                             |
        +------------------------------------------------+
                                 |
                                 v
                     +---------------------------+
                     |        SQLite DB          |
                     |   Stores Users & Tasks    |
                     +---------------------------+
```

## 🔐 Authentication Workflow
```
User Registers/Login
        |
        v
POST /auth/token  or  /auth/register
        |
        v
JWT Token Returned
        |
        v
Authorization: Bearer <token>
        |
        v
Access Protected Endpoints
```

## ⭐ 1. Project Description
  ⭐ 1. Project Description

This API provides functionality for:

✔ User Registration & Login (JWT)

✔ Creating, Reading, Updating, and Deleting tasks

✔ Viewing ONLY tasks created by logged-in user

✔ Advanced filtering (completed=true)

✔ Pagination (5 tasks/page)

✔ Swagger API documentation

✔ Admin access for all tasks

✔ Custom permissions to protect user data

✔ Unit tests included


## ⚙️ 2. Setup Instructions
### Activate Virtual Environment
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run Migrations
```
python manage.py migrate
```

### Start Server
```
python manage.py runserver
```

## 📌 3. API Endpoints
### Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /auth/register/ | Register user |
| POST | /auth/token/ | Login (JWT access + refresh) |
| POST | /auth/token/refresh/ | Refresh JWT token |

### Tasks
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /tasks/ | List tasks |
| POST | /tasks/ | Create task |
| GET | /tasks/<id>/ | Get task |
| PUT | /tasks/<id>/ | Update task |
| DELETE | /tasks/<id>/ | Delete task |

## 4. Filters & Pagination
```
/tasks/?page=2
/tasks/?completed=true
/tasks/?completed=false
```

## 5. API Docs
Swagger UI → http://127.0.0.1:8000/swagger/  

Includes:

All API routes

Request/Response schema

Live API testing

JWT integration

6. Permissions & Roles
👤 Regular User

Can create tasks

See only their tasks

Update only their tasks

Delete only their tasks

🛠 Admin User

Can view all tasks

Full system control


## 7. Tests
```
python manage.py test

Excepted Output``
Ran X tests in Y seconds
OK
`

## 8 Project Structure
```
task-manager-api/
│── taskmanager/
│── tasks/
│── manage.py
│── requirements.txt
│── .gitignore
```

9. Technology Stack

Python 3

Django

Django REST Framework

JWT Authentication (SimpleJWT)

SQLite

Swagger Documentation

## 👤 Author
**Gorank Kansal**
