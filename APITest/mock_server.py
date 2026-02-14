from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# -----------------------------
# In-memory database (mock DB)
# -----------------------------
mock_db = {
    1: {"id": 1, "name": "Admin", "role": "admin"},
    2: {"id": 2, "name": "User", "role": "user"}
}

# -----------------------------
# Basic Auth (test/test)
# -----------------------------
def check_auth(username, password):
    return username == "test" and password == "test"

def authenticate():
    return jsonify({"message": "Unauthorized"}), 401

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# -----------------------------
# GET endpoint
# -----------------------------
@app.route("/get_data/<int:user_id>", methods=["GET"])
@requires_auth
def get_data(user_id):
    user = mock_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


# -----------------------------
# POST endpoint
# -----------------------------
@app.route("/post_data", methods=["POST"])
@requires_auth
def post_data():
    data = request.json

    if not data or "name" not in data or "role" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    new_id = max(mock_db.keys()) + 1
    mock_db[new_id] = {"id": new_id, "name": data["name"], "role": data["role"]}

    return jsonify(mock_db[new_id]), 201


# -----------------------------
# Health check
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
