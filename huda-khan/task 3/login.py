users = [
    "ali@gmail.com",
    "sara@gmail.com",
    "ahmed@gmail.com"
]

email = input("Enter email: ").strip().lower()

if email in users:
    print("Login Successful")

else:
    print("User not found")