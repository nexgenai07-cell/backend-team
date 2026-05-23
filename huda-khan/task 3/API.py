import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print("Name:", data[0]["name"])
print("Email:", data[0]["email"])
