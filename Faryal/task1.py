#-------------------------------------------
#task1
#---------------------------------------------
classes = ("class 6A", "class 7B" , "classes 8c","class 9A")
print(classes[0])
classes[0] = "10 class"  # give error because tuple are immutable, once created cant changed 

#---------------------------------------------
# task 2
#---------------------------------------------
#Input marks in 3 subjects
math = int(input("Math marks: "))
science = int(input("Science marks: "))
english = int(input("English marks: "))
total = math + science + english

# Print formatted result card
print(f"\n{'Subject':<12} {'Marks':<6}")
print("-" * 20)
print(f"{'Math':<12} {math:>6}")
print(f"{'Science':<12} {science:>6}")
print(f"{'English':<12} {english:>6}")
print("-" * 20)
print(f"{'Total':<12} {total:>6}")

#--------------------------------------------
# task3
#-------------------------------------------
# Create dictionary with student names and fees paid
fees = {"Ali": 15000, "Sara": 0, "Umar": 8000}

# Add one new student
fees["Hina"] = 15000

# Update one fee
fees["Sara"] = 15000

# Delete one entry
del fees["Umar"]

# Display with status
for name, amount in fees.items():
    status = "Paid" if amount == 15000 else "Pending"
    print(f"{name}: Rs.{amount} - {status}")
    

#--------------------------------------------------
#task4
#---------------------------------------------------

age = int(input("Age: "))
prev_grade = input("Previous result (Pass/Fail): ")

# Check eligibility
if age < 5:
    print("Too young for admission.")
elif age > 15:
    print("Exceeds age limit.")
elif prev_grade.lower() != "pass":
    print("Must have passed previous class.")
else:
    print("Eligible for admission!")
    
#---------------------------------------------- 
# task 5 
#----------------------------------------------
# List of marks
marks = [78, 92, 65, 88, 71, 95, 60]

# Initialize variables
total = 0
highest = marks[0] # assume 78 is highest
lowest = marks[0] 

# Calculate using for loop
for m in marks:
    total += m
    if m > highest: # compare 78 with all values and replace if higher one is found
        highest = m
    if m < lowest:  # Fixed: was m < 1 lowest (syntax error)
        lowest = m

# Print summary
print(f"Total: {total}")
print(f"Average: {total/len(marks):.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")