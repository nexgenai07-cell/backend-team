# Day3 Python Assignment - All Tasks in One File

import json
import requests

# ------------------ Task 1: User Registration ------------------
def register_user(name, email, age):
    email = email.strip().lower()
    if name and age >= 18:
        return {"name": name, "email": email, "age": age}
    else:
        return "Invalid Input: Name empty or Age less than 18"

# ------------------ Task 2: User Class & Display ------------------
class User:
    def __init__(self, name, email, age, active=True):
        self.name = name
        self.email = email
        self.age = age
        self.active = active

    def __repr__(self):
        return f"Name: {self.name} | Email: {self.email} | Age: {self.age}"

# ------------------ Task 3: Active User Filtering ------------------
def filter_active(users):
    return [u for u in users if u.active]

# ------------------ Task 4: Search User by Email ------------------
def search_user(users, email):
    email = email.strip().lower()
    for u in users:
        if u.email == email:
            return f"User Found: {u.name}"
    return "User not found"

# ------------------ Task 5: File Handling ------------------
def save_users_to_file(users, filename="users.txt"):
    with open(filename, "w") as f:
        for u in users:
            f.write(f"{u.name}, {u.email}, {u.age}\n")

def read_users_from_file(filename="users.txt"):
    with open(filename, "r") as f:
        return f.read()

# ------------------ Task 6: JSON System ------------------
def save_users_to_json(users, filename="users.json"):
    data = [{"name": u.name, "email": u.email, "age": u.age} for u in users]
    with open(filename, "w") as f:
        json.dump(data, f)

def load_users_from_json(filename="users.json"):
    with open(filename, "r") as f:
        return json.load(f)

# ------------------ Task 7: API Integration ------------------
def fetch_api_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return [{"name": u["name"], "email": u["email"]} for u in response.json()]

# ------------------ Task 8: Mini Backend System ------------------
def merge_local_and_api(local_users):
    api_users = fetch_api_users()
    merged = [{"name": u.name, "email": u.email} for u in local_users] + api_users
    with open("merged.json", "w") as f:
        json.dump(merged, f)
    return merged

# ------------------ Task 9: Login System ------------------
def login(users, email):
    email = email.strip().lower()
    for u in users:
        if u.email == email:
            return "Login Successful"
    return "User not found"

# ------------------ Demo Run ------------------
if __name__ == "__main__":
    # Create sample users
    users = [
        User("Ali", "ali@gmail.com", 20),
        User("Sara", "sara@gmail.com", 22, active=False),
        User("Ahmed", "ahmed@gmail.com", 19)
    ]

    # Task 2 Display
    for u in users:
        print(u)

    # Task 3 Active Filter
    print("Active Users:", filter_active(users))

    # Task 4 Search
    print(search_user(users, "sara@gmail.com"))

    # Task 5 File Handling
    save_users_to_file(users)
    print(read_users_from_file())

    # Task 6 JSON
    save_users_to_json(users)
    print(load_users_from_json())

    # Task 7 API
    api_users = fetch_api_users()
    print("API Users Sample:", api_users[:1])

    # Task 8 Merge
    merged = merge_local_and_api(users)
    print("Merged Users:", merged[:3])

    # Task 9 Login
    print(login(users, "ali@gmail.com"))
