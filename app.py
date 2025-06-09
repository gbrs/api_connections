from flask import Flask, request, jsonify


app = Flask(__name__)

# Пример базы данных в памяти
data = {
    "users": [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
}

# GET (все пользователи)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data["users"])

# POST (добавить пользователя)
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    data["users"].append(new_user)
    return jsonify(new_user), 201

# PUT (обновить пользователя по id)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_updates = request.json
    for user in data["users"]:
        if user["id"] == user_id:
            user.update(user_updates)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# DELETE (удалить пользователя)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(data["users"]):
        if user["id"] == user_id:
            deleted_user = data["users"].pop(i)
            return jsonify(deleted_user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
