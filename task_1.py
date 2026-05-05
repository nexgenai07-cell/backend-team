# Task 1 Subject marks analyzer
Marks={"Math": 78, "Science": 45, "English": 60, "Urdu": 38, "Islamiat": 82}
Passing=[]
Failing=[]
# Using for loop to separate passed and failed subjects
for subject, mark in Marks.items():
    if mark >= 50:
        Passing.append(subject)
    else:
        Failing.append(subject)

# Printing the results
print("Passed subjects:", Passing)
print("Failed subjects:", Failing)

# ==============================================================
# Task 2 Absent student finder
all_students = ["Ali","Sara","Umar","Hina","Bilal","Zara"]
present = ["Ali", "Umar", "Bilal"]
# print the absent students
print("Absent students:")
# using for loop to find absent students
for student in all_students:
    if student not in present:
        print(student)

# ==============================================================
# Task 3 Attandance warning
# Get the attandance percentage from user
attandance=float(input("Enter the attandance percentage"))
# using conditions to check if the attandance is less than 75%
if attandance >= 75:
    print("Attandace is satisfactory")
elif attandance >=60:
    deficit=75-attandance
    print(f"Warning! Attendance low. Need {deficit:.1f}% more.")
else:
    print("Critical! Attendance is very low. Immediate action required.")
# ===============================================================
# Task 4 Teacher attandance log
# taking input from user for teacher name and status
teacher=input("Teacher name: ")
status=input("status (present/absent):")
date="2026-01-15"
# using conditions to check the status of teacher
if status.upper()=="present":
    status="present"
else:
    status="absent"
# printing the log
print(f"Teacher: {teacher}, Status: {status}, Date: {date}")
# ==============================================================
# Task 5 Teacher Info Dictionary
teacher = {
    "name": "Ms. Nadia",
    "subject": "Biology",
    "experience_years": 8,
    "is_hod": True
}
# printing the teacher information using for loop
for key, value in teacher.items():
    print(key, "->", value)
