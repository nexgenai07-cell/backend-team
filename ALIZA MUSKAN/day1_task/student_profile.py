# --- Student Profile Store Program ---
# Assigning values to variables with different data types
# String: Used for text (Must be enclosed in quotes)
student_name = "Ali Hassan" 
# Integer: Used for whole numbers (No decimal point)
roll_no = 101 
# Float: Used for decimal numbers
gpa = 3.75 

# Tuple: An ordered, immutable (unchangeable) collection .Identified by round brackets ()

subjects = ("Math", "Science", "English") 

# Dictionary: Stores data in Key:Value pairs .Identified by curly brackets {}
grades = {"Math": 90, "Science": 85, "English": 88} 

# --- Output Section ---
# The type() function identifies the data category of each variable

print("Name Type:", type(student_name))  # Output: <class 'str'>
print("GPA Type:", type(gpa))            # Output: <class 'float'>
print("Subjects Type:", type(subjects))  # Output: <class 'tuple'>
print("Grades Type:", type(grades))      # Output: <class 'dict'>

# Displaying the actual stored values
print("\n--- Student Summary ---")
print(f"Name: {student_name}")
print(f"Roll Number: {roll_no}")
print(f"Current GPA: {gpa}")
print(f"Enrolled Subjects: {subjects}")
print(f"Subject Scores: {grades}")