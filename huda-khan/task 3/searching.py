users = [
    {"name": "Ali", "email": "ali@gmail.com"},
    {"name": "Sara", "email": "sara@gmail.com"},
    {"name": "Ahmed", "email": "ahmed@gmail.com"}
]

search_email = input("Enter email: ").strip().lower()

found = False

for user in users:
    if user["email"] == search_email:
        print("User Found:", user["name"])
        found = True
        break

if found == False:
    print("User not found")