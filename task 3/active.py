users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Ahmed", "active": True}
]

for user in users:
    if user["active"] == True:
        print(user)