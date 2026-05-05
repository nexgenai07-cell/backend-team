# --- Grade Calculator Program ---

# Taking marks as input and converting to an integer
marks = int(input("Enter marks: "))

# Logic to determine the grade based on marks
if marks >= 90:      # Executes if marks are 90 or above
    grade = "A"
elif marks >= 80:     # Executes if marks are between 80 and 89
    grade = "B"
elif marks >= 70:    # Executes if marks are between 70 and 79
    grade = "C"
elif marks >= 60:    # Executes if marks are between 60 and 69
    grade = "D"
else:                # Executes if marks are below 60
    grade = "F"
# Printing the final result using an f-string
print(f"Grade: {grade}")