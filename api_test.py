"""
Question 1 — Validate GET API Responses
Problem:
Write a program to call a GET API endpoint using authentication and validate:

Response status code is 200

Response body contains a required key (e.g., "xyz")

Print the response JSON

Example:

Input: GET /get_data
Expected:
- Status code = 200
- JSON contains key "xyz"

Question 2 — Validate POST API Response

Problem:
Send a POST request with JSON payload and validate:

Status code is 200

Response contains expected field "xyz"

Payload is correctly processed by server
"""

import requests

auth = ("test","test")
headers = {"token":"bearer_token",
           "content-type":"application/json"}

get_url = "http://127.0.0.1:5000/get_data"

response = requests.post(get_url, auth=auth)
print(response.status_code)
print(response.json())

if response.status_code == 200:
    data=response.json()
    assert "xyz" in data
else:
    print("Get Request Failed")

post_url = "http://127.0.0.1:5000/post_data"
payload = {"test":"test", "xyz":"xyz"}
response = requests.post(post_url, data=payload, auth=auth)

if response.status_code == 200:
    print(response.status_code)
    data = response.json()
    assert "xyz" in data
else:
    print("Post Request Failed")
