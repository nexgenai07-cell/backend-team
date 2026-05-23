# Sample Data
users_data = [
    {"name": "Ali", "email": "ali@gmail.com", "age": 20},
    {"name": "Sara", "email": "sara@gmail.com", "age": 22},
    {"name": "Ahmed", "email": "ahmed@gmail.com", "age": 19}
]
file_name = "users.txt"
# --- STEP 1:EFFICIENT WRITING ---
with open(file_name, "w") as file:
    # Preparing all lines in one go and writing them instantly using writelines()
    file.writelines(f"{u['name']}, {u['email']}, {u['age']}\n" for u in users_data)

print("Data saved successfully")


# --- STEP 2:EFFICIENT READING ---
print("Output (Reading line-by-line):")
with open(file_name, "r") as file:
    # Direct loop over file object (Memory friendly)
    for line in file:
        print(line.strip())