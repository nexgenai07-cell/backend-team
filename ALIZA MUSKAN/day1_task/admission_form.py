# --- Student Admission Form Program ---
# Taking user input for student name (Stored as String)
name = input("Enter student name: ")

# Taking user input for age.We use int() to convert the input text into a whole number (Integer)
age = int(input("Enter age: "))
student_class = input("Enter class: ")

# --- Generating Formatted Admission Slip ---
# \n creates a new line for a cleaner look
print("\n--- Admission Slip ---")
# Using f-strings for clean concatenation and auto-conversion
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Class:{student_class}")
print("-----------------------")
print("\n--- Admission Slip ---")
# Using commas (,) to separate strings and variables
# Python will automatically add a single space between the label and the value
print("Name:", name)
print("Age:", age)
print("Class:", student_class)
print("-----------------------")