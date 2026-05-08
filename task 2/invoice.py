def generate_invoice(name, student_class, monthly_fee, months):
    total = monthly_fee * months

    if months > 10:
        surcharge = total * 0.05
        status = "LATE PAYMENT"
    else:
        surcharge = 0
        status = "PAID"

    grand_total = total + surcharge

    print("=== FEE INVOICE ===")
    print("Student :", name)
    print("Class :", student_class)
    print("Monthly :", monthly_fee)
    print("Months :", months)
    print("Subtotal :", total)
    print("Surcharge :", surcharge)
    print("Grand Total :", grand_total)
    print("Status :", status)


generate_invoice("Sara Malik", "10A", 3500, 12)
generate_invoice("Ali Hassan", "9B", 4000, 8)