users = []

name = input("Enter name: ").strip()
email = input("Enter email: ").strip().lower()
age = int(input("Enter age: "))

if name != "" and age >= 18:
    user = {
        "name": name,
        "email": email,
        "age": age
    }

    users.append(user)

    print("User Registered Successfully")

else:
    print("Invalid Input: Name empty or Age less than 18")