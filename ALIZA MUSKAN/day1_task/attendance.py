# --- Class Attendance Roll Call Program ---

# Creating a list of 5 student names
students = ["Ali","Sara","Umar","Hina","Bilal"]

print("--- Attendance Roll Call ---")
"""
 The for loop goes through each item in the list
 enumerate() provides both the count (roll) and the item (name)
start=1 ensures our numbering starts from 1 instead of 0
"""
for roll, name in enumerate(students, start=1):
    # Using f-string to print formatted roll number and name
    print(f"{roll}. {name}")