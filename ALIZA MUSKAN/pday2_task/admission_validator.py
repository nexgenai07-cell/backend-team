# 1. DATABASE: A list of students already registered in the system
enrolled_students = ["ALI HASSAN", "SARA MALIK", "USMAN KHAN"]
print("--- UNIVERSITY ADMISSION SYSTEM ---")

# 2. INPUT & CLEANING: Remove extra spaces and make it UPPERCASE
raw_input_name = input("Enter Student Name: ")
cleaned_name = raw_input_name.strip().upper()

# 3. CNIC VALIDATION: This loop keeps asking until the input is correct
while True:
    cnic = input("Enter 13-digit CNIC: ").strip()
    # Check if input is only numbers AND length is exactly 13
    if cnic.isdigit() and len(cnic) == 13:
        print("CNIC Validated Successfully.")
        break  # Exit the loop because the input is correct
    else:
        print("ERROR: CNIC must be 13 digits. Please try again.")

# 4. ENROLLMENT CHECK: Searching the name in our list
is_enrolled = cleaned_name in enrolled_students
# 5. FINAL OUTPUT: Displaying the result simply
print("\n--- ADMISSION STATUS REPORT ---")
print("Name (Cleaned)  :", cleaned_name)
print("Name (Display)  :", cleaned_name.title()) # Converts 'ALI' to 'Ali'
print("CNIC Number     :", cnic)
print("CNIC Validity   : YES (Verified)")
# Final Decision Logic
if is_enrolled:
    print("Enrolled Status : YES")
    print("Final Status    : EXISTING STUDENT")
else:
    print("Enrolled Status : NO")
    print("Final Status    : NEW ADMISSION GRANTED")
print("-------------------------------")