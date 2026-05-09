users = [
    "Ali, ali@gmail.com, 20",
    "Sara, sara@gmail.com, 22",
    "Ahmed, ahmed@gmail.com, 19"
]

# Save in file
with open("users.txt", "w") as file:
    for user in users:
        file.write(user + "\n")

# Read file
with open("users.txt", "r") as file:
    data = file.read()
    print(data)