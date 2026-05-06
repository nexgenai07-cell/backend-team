records = {
    101: "Ali Hassan",
    102: "Sara Ahmed"
}

success = 0
errors = 0

while True:
    roll = input("Roll or done: ")

    if roll == "done":
        break

    try:
        roll = int(roll)

        if roll not in records:
            raise KeyError

        amount = float(input("Amount: "))

        if amount < 0 or amount > 10000:
            raise ValueError

        print("SUCCESS:", records[roll], amount)
        success += 1

    except ValueError:
        print("Invalid amount")
        errors += 1

    except KeyError:
        print("Roll not found")
        errors += 1

print("Successful:", success)
print("Errors:", errors)