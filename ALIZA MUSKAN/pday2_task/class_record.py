# 1. DATABASE: A nested structure (Dictionary -> List -> Dictionary)
school_data = {
    "Class 8B": [
        {"name": "Sara Ahmed", "roll": 3, "marks": 85, "fee_paid": False},
        {"name": "Ali Khan", "roll": 5, "marks": 92, "fee_paid": True}
    ],
    "Class 9A": [
        {"name": "Kamil Baig", "roll": 10, "marks": 97, "fee_paid": True},
        {"name": "Umar Farooq", "roll": 7, "marks": 78, "fee_paid": False}
    ]
}
# --- FUNCTION 1: Add a new student record ---
def add_student(class_key, s_name, s_roll, s_marks, s_fee):
    # Pack student details into a new dictionary
    new_entry = {"name": s_name, "roll": s_roll, "marks": s_marks, "fee_paid": s_fee}
    # Check if the class exists, then add the record to that list
    if class_key in school_data:
        school_data[class_key].append(new_entry)
        print("Student added successfully.")
    else:
        print("Error: Class not found.")
# --- FUNCTION 2: Find the Top Scorer ---
def find_top_scorer():
    best_marks = -1
    best_student = None
    student_class = ""
    # Loop through each class in the database
    for class_name, student_list in school_data.items():
        # Loop through each student in the current class list
        for student in student_list:
            # Compare current student's marks with the record
            if student["marks"] > best_marks:
                best_marks = student["marks"]
                best_student = student
                student_class = class_name     
    return best_student, student_class

# --- FUNCTION 3: List students with unpaid fees ---
def show_defaulters():
    print("--- FEE DEFAULTERS ---")
    count = 0
    # Search all classes and all students
    for class_name, student_list in school_data.items():
        for student in student_list:
            # Check if fee_paid is False
            if student["fee_paid"] == False:
                count = count + 1
                print(count, "-", student["name"], "from", class_name)
    print("Total Defaulters:", count)

# --- EXECUTION (Running the System) ---

# Step 1: Add a new student with high marks
add_student("Class 9A", "Zain Ahmed", 12, 99, True)
print(school_data)
# Ste9p 2: Get and print the top scorer result
top_s, t_class = find_top_scorer()
print("\n--- TOP SCORER RESULT ---")
print("Name:", top_s["name"])
print("Class:", t_class)
print("Marks:", top_s["marks"])
# Step 3: Show the list of defaulters
show_defaulters()