Flask REST API
Overview

A Python REST API built with Flask to demonstrate how HTTP methods can be used to create, retrieve, update, and delete user data.

The project uses JSON data and provides multiple API endpoints for user management.

Technologies
Python
Flask
REST API
JSON
HTTP Methods
API Operations

The API demonstrates the following HTTP methods:

Method	Endpoint	Description
GET	/users	Retrieve all users
GET	/users/<id>	Retrieve a specific user
POST	/users	Create a new user
PUT	/users/<id>	Update a complete user
PATCH	/users/<id>	Partially update a user
DELETE	/users/<id>	Delete a user
Project Structure
flask-rest-api/
│
├── README.md
├── app.py
├── requirements.txt
└── .gitignore
Installation

Clone the repository and install the required dependency:

pip install -r requirements.txt
Running the API

Run:

python app.py

The API will run locally at:

http://localhost:5000
Example Requests
Get all users
GET /users
Get a specific user
GET /users/3
Create a user
POST /users

Example JSON:

{
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com"
}
Update a user
PUT /users/3
Partially update a user
PATCH /users/3
Delete a user
DELETE /users/3
Skills Demonstrated
Python programming
Flask
REST API development
JSON handling
HTTP methods
CRUD operations
Request handling
API routing
HTTP status codes
Author

Hany Talaat
