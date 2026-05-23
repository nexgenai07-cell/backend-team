classes = {
    "Class 8B": [
        {"name": "Sara Ahmed", "roll": 3, "marks": 67, "fee_paid": False}
    ],
    "Class 9A": [
        {"name": "Kamil Baig", "roll": 1, "marks": 97, "fee_paid": True},
        {"name": "Umar Farooq", "roll": 7, "marks": 72, "fee_paid": False}
    ]
}

classes["Class 9A"].append(
    {"name": "Ali Hassan", "roll": 8, "marks": 88, "fee_paid": True}
)

top_name = ""
top_marks = 0
top_class = ""

for cls in classes:
    for s in classes[cls]:
        if s["marks"] > top_marks:
            top_marks = s["marks"]
            top_name = s["name"]
            top_class = cls

print("Topper:", top_name, top_class, top_marks)

print("Fee Defaulters:")
for cls in classes:
    for s in classes[cls]:
        if s["fee_paid"] == False:
            print(s["name"], "|", cls)