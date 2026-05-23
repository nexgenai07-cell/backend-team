# 1. DATABASE: List of 15 students with their fee status
students = [
    {"name": "Ali Hassan", "fee_paid": True},
    {"name": "Sara Ahmed", "fee_paid": False},
    {"name": "Umar Khan", "fee_paid": True},
    {"name": "Zainab Bibi", "fee_paid": True},
    {"name": "Bilal Raza", "fee_paid": True},
    {"name": "Hamza Ali", "fee_paid": False},
    {"name": "Dua Fatimah", "fee_paid": True},
    {"name": "Ahmed Raza", "fee_paid": True},
    {"name": "Sana Malik", "fee_paid": True},
    {"name": "Zohaib Khan", "fee_paid": True},
    {"name": "Kashif Ali", "fee_paid": True},
    {"name": "Maryum Bibi", "fee_paid": True},
    {"name": "Usman Sheikh", "fee_paid": False},
    {"name": "Fahad Mustafa", "fee_paid": True},
    {"name": "Hina Dilpazeer", "fee_paid": True}
]
# 2. Setup counters
seat_number = 0
students_seated = 0
print("=== EXAM HALL SEATING CHART ===")
# 3. Loop through the students
for s in students:

    # Check if hall is full (Max 10 students)
    if students_seated == 10:
        print("--- Hall Full. Stopping. ---")
        break # Exit the loop completely
    
    # Check if fees are NOT paid
    if s["fee_paid"] == False:
        print("       :", s["name"], "[BLOCKED - Fee Pending]")
        continue # Skip to the next student in the list
    
    # If fees are paid, assign a seat
    seat_number = seat_number + 1
    students_seated = students_seated + 1
    print("Seat", seat_number, ":", s["name"], "[SEATED]")

# 4. Final Calculation
not_seated = len(students) - students_seated
print("-------------------------------")
print("Total students not seated:", not_seated)