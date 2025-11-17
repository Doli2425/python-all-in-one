import requests

# GET Method 요청
url = "https://jsonplaceholder.typicode.com/users"

resp = requests.delete(url)
print(resp.headers)
print(resp.text)

