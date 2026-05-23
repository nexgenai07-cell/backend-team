# 1. DATABASE: Students mapped by their Roll Numbers
students_db = {
    "101": "Ali Hassan",
    "102": "Sara Ahmed",
    "103": "Umar Khan"
}
# Counters for final summary
success_count = 0
error_count = 0
print("--- FEE ENTRY SYSTEM ---")
while True:
    print("\nEnter Roll Number (or type 'done' to finish):")
    roll = input().strip()
    # Exit condition
    if roll.lower() == 'done':
        break
    
    try:
        # (a) Check if Roll Number exists in our Dictionary
        if roll not in students_db:
            # Manually raising a KeyError for missing roll number
            raise KeyError
        name = students_db[roll]
        # (b) Get Amount and check for ValueError
        print("Enter Amount:")
        amount_raw = input().strip()
        amount = int(amount_raw) # This line will fail if input is 'abc'
        
        # (c) Custom check for negative or excessive amount
        if amount < 0 or amount > 100000:
            print("ERROR: Amount must be between 0 and 100,000.")
            error_count = error_count + 1
        else:
            print("SUCCESS:", name, "| Rs.", amount, "recorded.")
            success_count = success_count + 1
    except ValueError:
        # Occurs if int() conversion fails (e.g., user types 'abc')
        print("ERROR: Invalid amount. Numbers only.")
        error_count = error_count + 1
    except KeyError:
        # Occurs if roll number is not in students_db
        print("ERROR: Roll", roll, "not found.")
        error_count = error_count + 1
# 2. FINAL SUMMARY
print("\n--- Summary ---")
print("Successful :", success_count)
print("Errors     :", error_count)