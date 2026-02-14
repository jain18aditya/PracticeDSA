"""
2xProblem: API Automation — Positive & Negative Testing

You are given a local mock API server running at:

    http://127.0.0.1:5000

The server exposes the following endpoints:

1. GET /get_data/<id>
   - Requires Basic Auth (username: test, password: test)
   - Returns user data if ID exists
   - Returns:
        200 → Success
        401 → Unauthorized
        404 → User not found

2. POST /post_data
   - Requires Basic Auth
   - Accepts JSON payload:
        {
            "name": string,
            "role": string
        }
   - Returns:
        201 → Data created successfully
        400 → Invalid payload / missing field
        401 → Unauthorized

Tasks:

1. Positive Tests
   - Send GET request with valid auth and valid ID → expect 200
   - Send POST request with valid payload → expect 201

2. Negative Tests
   - Wrong authentication → expect 401
   - Missing required field in POST → expect 400
   - Invalid user ID → expect 404
   - Empty JSON payload → expect 400

3. Validate:
   - Status codes
   - Response JSON
   - Required fields in response

Goal:
Write a script that automates the above API tests using Python requests library.
"""
import requests

BASE_URL = "http://127.0.0.1:5000"
VALID_AUTH = ("test", "test")

# -------------------------
# 1. GET SUCCESS
# -------------------------
print("\n--- GET SUCCESS ---")
r = requests.get(f"{BASE_URL}/get_data/1", auth=VALID_AUTH)
print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 200
assert "name" in r.json()

# -------------------------
# 2. POST SUCCESS
# -------------------------
print("\n--- POST SUCCESS ---")
payload = {"name": "tester", "role": "tester"}

r = requests.post(
    f"{BASE_URL}/post_data",
    json=payload,
    auth=VALID_AUTH
)

print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 201
assert r.json()["name"] == "tester"

# -------------------------
# 3. WRONG AUTH → 401
# -------------------------
print("\n--- WRONG AUTH TEST ---")
r = requests.get(f"{BASE_URL}/get_data/1", auth=("wrong", "wrong"))
print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 401

# -------------------------
# 4. MISSING FIELD → 400
# -------------------------
print("\n--- MISSING FIELD TEST ---")
payload = {"name": "missing_role"}

r = requests.post(
    f"{BASE_URL}/post_data",
    json=payload,
    auth=VALID_AUTH
)

print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 400

# -------------------------
# 5. INVALID ID → 404
# -------------------------
print("\n--- INVALID ID TEST ---")
r = requests.get(f"{BASE_URL}/get_data/999", auth=VALID_AUTH)
print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 404

# -------------------------
# 6. EMPTY JSON → 400
# -------------------------
print("\n--- EMPTY JSON TEST ---")
r = requests.post(
    f"{BASE_URL}/post_data",
    json={},
    auth=VALID_AUTH
)

print("Status:", r.status_code)
print("Response:", r.json())
assert r.status_code == 400

print("\n All tests passed successfully!")
