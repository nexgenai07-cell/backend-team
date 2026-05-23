users_database = [
    {'name': 'Ali', 'email': 'ali@gmail.com'},
    {'name': 'Sara', 'email': 'sara@gmail.com'},
    {'name': 'Ahmed', 'email': 'ahmed@gmail.com'}
]
print("--- Search User by Email ---")
search_email = input("Enter email to search(must add @gmail.com): ").strip().lower()
for user in users_database:
    if user['email'] == search_email:
        print("\nOutput:")
        print(f"User Found: {user['name'] }")
        break  # If found, break the loop immediately
else:
    print("Output:")
    print("User not found")