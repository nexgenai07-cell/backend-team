import json  # Importing Python's built-in module for JSON handling
users_data = [
    {"name": "Ali", "email": "ali@gmail.com"}
]
file_name = "users.json" 
# --- STEP 1: CONVERT TO JSON AND SAVE ---
with open(file_name, "w") as file:

    json.dump(users_data, file)

print("Data saved as JSON successfully!")
# print(file)

# --- STEP 2: LOAD JSON AND DISPLAY ---
print("Output (Loaded Python Data):")
with open(file_name, "r") as file:
    loaded_data = json.load(file)
print(loaded_data)

