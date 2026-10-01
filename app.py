from flask import Flask, jsonify, request


app = Flask(__name__)


users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv"
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net"
    }
]


# GET - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "username": data["username"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201


# GET - Get a single user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next(
        (user for user in users if user["id"] == id),
        None
    )

    if user:
        return jsonify(user), 200

    return jsonify({
        "message": "User not found"
    }), 404


# PUT - Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json

    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            user["username"] = data["username"]
            user["email"] = data["email"]

            return jsonify({
                "message": "User updated successfully",
                "user": user
            }), 200

    return jsonify({
        "message": "User not found"
    }), 404


# PATCH - Partially update a user
@app.route('/users/<int:id>', methods=['PATCH'])
def patch_user(id):
    data = request.json

    for user in users:
        if user["id"] == id:

            if "name" in data:
                user["name"] = data["name"]

            if "username" in data:
                user["username"] = data["username"]

            if "email" in data:
                user["email"] = data["email"]

            return jsonify({
                "message": "User updated successfully",
                "user": user
            }), 200

    return jsonify({
        "message": "User not found"
    }), 404


# DELETE - Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)

            return jsonify({
                "message": "User deleted successfully"
            }), 200

    return jsonify({
        "message": "User not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
