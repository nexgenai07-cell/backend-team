class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

user1 = User("Ali", "ali@gmail.com", 20)
user2 = User("Sara", "sara@gmail.com", 22)
user3 = User("Ahmed", "ahmed@gmail.com", 19)

users = [user1, user2, user3]

for user in users:
    print(f"Name: {user.name} | Email: {user.email} | Age: {user.age}")