# Input student age and previous grade
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