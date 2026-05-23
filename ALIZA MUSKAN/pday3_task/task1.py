# Initialize an empty list to act as our database for registered users
database = []
print("---User Registration System ---")

# Step 1: Taking inputs and cleaning them instantly
name = input("Enter Name: ").strip()
email = input("Enter Email: ").strip().lower()
age_input = input("Enter Age: ")
# Using try-except ensures the program won't crash if the user types letters instead of numbers
try:
    age = int(age_input)
except ValueError:
    age = 0 
# Checking: Name is not empty, Age is 18+, and Email contains both '@' and '.'
if name != "" and age >= 18 and "@" in email and ".com" in email:
    # Step 4: Storing data professionally using a Dictionary
    user_data = {
        "name": name,
        "email": email,
        "age": age
    }
    database.append(user_data)
    print("Output:")
    print("User Registered Successfully")
    print("Database State:", database)

else:
    print("Output:")
    print("Invalid Input: Please ensure Name is not empty, Age is 18 or above, and Email format is correct.")

    #print(database)