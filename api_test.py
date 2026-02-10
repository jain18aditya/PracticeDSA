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
