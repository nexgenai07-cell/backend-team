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