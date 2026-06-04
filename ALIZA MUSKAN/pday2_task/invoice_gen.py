def generate_invoice(student_name, student_class, monthly_fee, months):
    """
    This function calculates the fee and returns a dictionary.
    """
    # 1. Basic calculation
    subtotal = monthly_fee * months
    # 2. Apply 5% surcharge if months are more than 10
    if months > 10:
        surcharge = subtotal * 0.05
        status = "LATE PAYMENT"
    else:
        surcharge = 0
        status = "ON TIME"
    # 3. Final calculation
    grand_total = subtotal + surcharge

    # 4. Returning data in a dictionary format
    return {
        "Student": student_name,
        "Class": student_class,
        "Monthly": monthly_fee,
        "Months": months,
        "Subtotal": subtotal,
        "Surcharge": surcharge,
        "Grand Total": grand_total,
        "Status": status
    }
# --- MAIN PROGRAM ---
# Task requirement: Call the function twice with different data
# Invoice 1: Late Case (Months > 10)
print("=== FEE INVOICE 1 ===")
inv1 = generate_invoice("Sara Malik", "10A", 3500, 12)
for key, value in inv1.items():
    print(f"{key}: {value}")

# Invoice 2: On-Time Case (Months <= 10)
print("=== FEE INVOICE 2 ===")
inv2 = generate_invoice("Ali Ahmed", "9B", 4000, 8)
for key, value in inv2.items():
    print(f"{key}: {value}")

    # --- User inputs---

print("\n--- ENTER STUDENT DETAILS ---")

# 1. Text input ke liye simple input()
name_input = input("Enter Student Name: ")
class_input = input("Enter Class: ")

fee_input = int(input("Enter Monthly Fee: "))
months_input = int(input("Enter Number of Months: "))

user_invoice = generate_invoice(name_input, class_input, fee_input, months_input)
print("\n=== YOUR GENERATED INVOICE ===")
for key, value in user_invoice.items():
    print(f"{key}: {value}")