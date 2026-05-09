# Day 2 Python Practice Tasks
# Topics: Functions, Strings, Nested Data, Loop Control,
# Error Handling, List Comprehension, Logic Building
# -------------------------------
# Task 1 - Fee Invoice Generator
# Hint: Use an if inside the function to check months > 10 for surcharge
# -------------------------------

def generate_invoice(student, class_name, monthly_fee, months):
    # Calculate subtotal
    subtotal = monthly_fee * months
    
    # Initialize surcharge and status
    surcharge = 0
    status = "ON TIME"
    
    # Apply 5% surcharge if months > 10
    if months > 10:
        surcharge = subtotal * 0.05
        status = "LATE PAYMENT"
    
    # Grand total = subtotal + surcharge
    grand_total = subtotal + surcharge
    
    # Return dictionary as invoice
    return {
        "student": student,
        "class": class_name,
        "monthly": monthly_fee,
        "months": months,
        "subtotal": subtotal,
        "surcharge": surcharge,
        "grand_total": grand_total,
        "status": status
    }

# Example calls
print("=== FEE INVOICE ===")
print(generate_invoice("Sara Malik", "Class 10A", 3500, 12))
print(generate_invoice("Ali Hassan", "Class 9B", 3000, 8))


# -------------------------------
# Task 2 - Admission Validator
# Hint: Use .strip().upper() for cleaning, .isdigit() + len() for CNIC check
# -------------------------------

def admission_validator(name, cnic, enrolled_list):
    # Clean input
    cleaned_name = name.strip().upper()
    display_name = cleaned_name.title()
    
    # CNIC validation: must be 13 digits
    cnic_valid = cnic.isdigit() and len(cnic) == 13
    
    # Check enrollment
    enrolled = cleaned_name in enrolled_list
    
    status = "EXISTING STUDENT" if enrolled else "NEW STUDENT"
    
    return {
        "Name (cleaned)": cleaned_name,
        "Name (display)": display_name,
        "CNIC": cnic,
        "CNIC Valid": "YES" if cnic_valid else "NO",
        "Enrolled": "YES" if enrolled else "NO",
        "Status": status
    }

students = ["ALI HASSAN", "SARA MALIK", "KAMIL BAIG"]
print(admission_validator("ali hassan", "3520112345678", students))


# -------------------------------
# Task 3 - Multi-Class Record System
# Hint: Loop: for class_name, students in data.items()
# -------------------------------

data = {
    "Class 9A": [
        {"name":"Kamil Baig","roll":1,"marks":97,"fee_paid":True},
        {"name":"Umar Farooq","roll":7,"marks":65,"fee_paid":False}
    ],
    "Class 8B": [
        {"name":"Sara Ahmed","roll":3,"marks":72,"fee_paid":False}
    ]
}

def top_scorer(data):
    topper = None
    for cls, students in data.items():
        for s in students:
            if topper is None or s["marks"] > topper["marks"]:
                topper = {**s, "class":cls}
    return topper

def fee_defaulters(data):
    defaulters = []
    for cls, students in data.items():
        for s in students:
            if not s["fee_paid"]:
                defaulters.append((s["name"], cls, s["roll"]))
    return defaulters

print("=== TOP SCORER ===")
print(top_scorer(data))
print("=== FEE DEFAULTERS ===")
print(fee_defaulters(data))


# -------------------------------
# Task 4 - Exam Hall Seating System
# Hint: Use continue to skip fee defaulters, break when hall full
# -------------------------------

students = [
    {"name":"Ali Hassan","fee_paid":True},
    {"name":"Sara Ahmed","fee_paid":False},
    {"name":"Umar Khan","fee_paid":True},
    {"name":"Bilal Raza","fee_paid":True},
    # ... add more students up to 15
]

seat_count = 0
for s in students:
    if not s["fee_paid"]:
        print(f"{s['name']} [BLOCKED - Fee Pending]")
        continue
    seat_count += 1
    print(f"Seat {seat_count}: {s['name']} [SEATED]")
    if seat_count == 10:
        print("Hall Full. Remaining students not seated.")
        break


# -------------------------------
# Task 5 - Fee Entry with Error Recovery
# Hint: Put try-except inside while loop, catch ValueError, KeyError, custom check
# -------------------------------

db = {101:"Ali Hassan", 102:"Sara Ahmed"}
success, errors = 0, 0

while True:
    roll = input("Roll (or 'done'): ")
    if roll.lower() == "done":
        break
    try:
        roll = int(roll)
        if roll not in db:
            raise KeyError
        amount = input("Amount: ")
        if not amount.isdigit():
            raise ValueError
        amount = int(amount)
        if amount <= 0 or amount > 100000:
            raise Exception("Invalid amount range")
        print(f"SUCCESS: {db[roll]} | Rs. {amount}")
        success += 1
    except ValueError:
        print("ERROR: Invalid amount. Numbers only.")
        errors += 1
    except KeyError:
        print(f"ERROR: Roll {roll} not found.")
        errors += 1
    except Exception as e:
        print(f"ERROR: {e}")
        errors += 1

print(f"\nSuccessful: {success}\nErrors: {errors}")


# -------------------------------
# Task 6 - Report Generator with Comprehensions
# Hint: Use list comprehensions ONLY
# -------------------------------

students = [
    {"name":"Ali","marks":88,"fee_paid":True,"class":"9"},
    {"name":"Sara","marks":45,"fee_paid":False,"class":"8"},
    {"name":"Kamil","marks":97,"fee_paid":True,"class":"9"},
]

high_scorers = [s["name"] for s in students if s["marks"] > 75]
pass_fail = [(s["name"], "PASS" if s["marks"]>=50 else "FAIL") for s in students]
class9_fee_paid = [s["name"] for s in students if s["class"]=="9" and s["fee_paid"]]
marks_percentage = [f"{s['name']}: {s['marks']}/150 = {round((s['marks']/150)*100,1)}%" for s in students]

print("High Scorers:", high_scorers)
print("Pass/Fail:", pass_fail)
print("Class 9 Fee-Paid:", class9_fee_paid)
print("Marks %:", marks_percentage)


# -------------------------------
# Task 7 - Student Analytics Engine
# Hint: Manual loops for max/min, dict for count, filter for eligibility, partial search
# -------------------------------

students = [
    {"name":"Ali Hassan","class":"9B","marks":88,"fee_paid":True,"attendance":80},
    {"name":"Zara Siddiq","class":"10","marks":41,"fee_paid":True,"attendance":70},
    {"name":"Kamil Baig","class":"9A","marks":97,"fee_paid":True,"attendance":90},
]

# Topper & Lowest
topper, lowest = students[0], students[0]
for s in students:
    if s["marks"] > topper["marks"]: topper = s
    if s["marks"] < lowest["marks"]: lowest = s

# Count per class
class_count = {}
for s in students:
    class_count[s["class"]] = class_count.get(s["class"],0)+1

# Exam eligible
eligible = [s for s in students if s["attendance"]>=75 and s["fee_paid"]]

# Search partial
search = "ali"
search_results = [s for s in students if search in s["name"].lower()]

# Class-wise average
class_avg = {}
for s in students:
    cls = s["class"]
    class_avg.setdefault(cls, []).append(s["marks"])
class_avg = {cls: sum(m)/len(m) for cls,m in class_avg.items()}

print(" ANALYTICS REPORT ")
print("Topper:", topper)
print("Lowest:", lowest)
print("Class Count:", class_count)
print("Eligible:", eligible)
print("Search Results:", search_results)
print("Class Avg:", class_avg)
