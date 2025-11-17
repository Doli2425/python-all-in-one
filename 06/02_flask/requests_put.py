import requests

# GET Method 요청
url = "https://jsonplaceholder.typicode.com/users"
data = {"name": "Bob"}

resp = requests.put(url, json=data)
print(resp.headers)
print(resp.text)
