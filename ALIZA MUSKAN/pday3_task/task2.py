# Step 1: Define the User class with a built-in string representation
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    # The __str__ method defines how the object should be printed automatically
    def __str__(self):
        return f"Name: {self.name} | Email: {self.email} | Age: {self.age}"
    
user1=User("Ali", "ali@gmail.com", 20)
user2=User("Sara", "sara@gmail.com", 22)
user3=User("Ahmed", "ahmed@gmail.com", 19)

# Step 2 & 3: Create users and store them directly in a list to save memory/lines
users_database = [
   user1,user2,user3
]
print("--- User Data Display ---")
print("Output:")
# Step 4: Extremely clean loop
# Because of __str__, Python automatically formats each user object when printed
for user in users_database:
    print(user)