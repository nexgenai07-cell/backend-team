# Day 3 Python Tasks

# ------------------ Task 1: User Registration ------------------
users = []

name = "Ali"
email = "ALI@GMAIL.COM".strip().lower()
age = 20

if name and age >= 18:
    users.append({"name": name, "email": email, "age": age})
    print("User Registered Successfully")
else:
    print("Invalid Input: Name empty or Age less than 18")

# ------------------ Task 2: User Class ------------------
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

users_list = [
    User("Ali", "ali@gmail.com", 20),
    User("Sara", "sara@gmail.com", 22),
    User("Ahmed", "ahmed@gmail.com", 19)
]

for u in users_list:
    print(f"Name: {u.name} | Email: {u.email} | Age: {u.age}")

# ------------------ Task 3: Active User Filtering ------------------
users_active = [{'name':'Ali','active':True},{'name':'Sara','active':False}]
for u in users_active:
    if u['active']:
        print(u)

# ------------------ Task 4: Search User by Email ------------------
users_search = [{"name":"Sara","email":"sara@gmail.com"}]
search_email = "sara@gmail.com"
found = False
for u in users_search:
    if u["email"] == search_email:
        print(f"User Found: {u['name']}")
        found = True
        break
if not found:
    print("User not found")

# ------------------ Task 5: File Handling ------------------
users_file = [
    {"name":"Ali","email":"ali@gmail.com","age":20},
    {"name":"Sara","email":"sara@gmail.com","age":22},
    {"name":"Ahmed","email":"ahmed@gmail.com","age":19}
]

with open("users.txt", "w") as f:
    for u in users_file:
        f.write(f"{u['name']}, {u['email']}, {u['age']}\n")

with open("users.txt", "r") as f:
    print(f.read())

# ------------------ Task 6: JSON System ------------------
import json
users_json = [{"name":"Ali","email":"ali@gmail.com"}]
with open("users.json", "w") as f:
    json.dump(users_json, f)
with open("users.json", "r") as f:
    data = json.load(f)
    print(data)

# ------------------ Task 7: API Integration ------------------
import requests   # for API calls
import json       # for JSON handling (needed in Task 8)

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

for user in data[:1]:
    print("Name:", user["name"])
    print("Email:", user["email"])

# ------------------ Task 8: Mini Backend System ------------------
class UserMini:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Local users
local_users = [UserMini("Ali","ali@gmail.com"), UserMini("Sara","sara@gmail.com")]

# API users
api_data = requests.get("https://jsonplaceholder.typicode.com/users").json()
api_users = [UserMini(u["name"], u["email"]) for u in api_data[:1]]

# Merge local + API users
all_users = local_users + api_users

# Save JSON
with open("all_users.json","w") as f:
    json.dump([u.__dict__ for u in all_users], f)

# Display merged users
for u in all_users:
    print(f"{u.name} - {u.email}")


# ------------------ Task 9: Login System ------------------
users_login = [{"email":"ali@gmail.com"},{"email":"sara@gmail.com"}]
login_email = "ALI@GMAIL.COM".strip().lower()
found = any(u["email"] == login_email for u in users_login)
if found:
    print("Login Successful")
else:
    print("User not found")
