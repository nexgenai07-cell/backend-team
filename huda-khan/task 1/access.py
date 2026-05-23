role = input("Enter role: ").lower()

if role == "principal":
    print("Access: All modules (Students, Fees, Staff, Reports)")
elif role == "teacher":
    print("Access: Students, Attendance, Marks")
elif role == "student":
    print("Access: Own profile, Fee status, Result")
else:
    print("Unknown role. Access denied.")
    