# List of marks
marks = [78, 92, 65, 88, 71, 95, 60]

# Initialize variables
total = 0
highest = marks[0]
lowest = marks[0]

# Calculate using for loop
for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:  # Fixed: was m < 1 lowest (syntax error)
        lowest = m

# Print summary
print(f"Total: {total}")
print(f"Average: {total/len(marks):.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")