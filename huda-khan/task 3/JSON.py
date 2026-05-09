import json

users = [
    {
        "name": "Ali",
        "email": "ali@gmail.com"
    }
]

# Save JSON
with open("users.json", "w") as file:
    json.dump(users, file)

# Load JSON
with open("users.json", "r") as file:
    data = json.load(file)

print(data)