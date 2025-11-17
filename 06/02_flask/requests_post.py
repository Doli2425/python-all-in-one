import requests

# GET Method 요청
url = "https://jsonplaceholder.typicode.com/users"
data = {"name": "Alice", "email": "alice@example.com"}

resp = requests.post(url, json=data)

print(resp.headers)
print(resp.text)
