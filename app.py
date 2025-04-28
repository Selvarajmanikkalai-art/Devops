from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
