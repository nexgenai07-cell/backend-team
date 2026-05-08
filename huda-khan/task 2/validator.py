students = ["ALI HASSAN", "SARA MALIK", "UMAR KHAN"]

name = input("Enter name: ").strip().upper()
cnic = input("Enter CNIC: ").strip()

valid = cnic.isdigit() and len(cnic) == 13

print("Name (cleaned):", name)
print("Name (display):", name.title())
print("CNIC:", cnic)
print("CNIC Valid:", "YES" if valid else "NO")

if name in students:
    print("Enrolled: YES")
    print("Status: EXISTING STUDENT")
else:
    print("Enrolled: NO")
    print("Status: NEW STUDENT")