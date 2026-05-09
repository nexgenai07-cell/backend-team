import json
import requests

# User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Local users
local_users = [
    User("Ali", "ali@gmail.com"),
    User("Sara", "sara@gmail.com")
]

# API users
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
api_data = response.json()

# Merge data
all_users = []

for user in local_users:
    all_users.append({
        "name": user.name,
        "email": user.email
    })

for user in api_data[:1]:
    all_users.append({
        "name": user["name"],
        "email": user["email"]
    })

# Save JSON
with open("all_users.json", "w") as file:
    json.dump(all_users, file)

# Load JSON
with open("all_users.json", "r") as file:
    data = json.load(file)

# Display
for user in data:
    print(user["name"], "-", user["email"])