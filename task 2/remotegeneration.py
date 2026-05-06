students = [
    {"name": "Ali", "marks": 88, "fee_paid": True, "class": 9},
    {"name": "Sara", "marks": 45, "fee_paid": False, "class": 9},
    {"name": "Noor", "marks": 81, "fee_paid": True, "class": 10},
    {"name": "Hina", "marks": 76, "fee_paid": True, "class": 8}
]

high = [x["name"] for x in students if x["marks"] > 75]

result = [(x["name"], "PASS" if x["marks"] >= 50 else "FAIL") for x in students]

fee_paid = [x["name"] for x in students if x["class"] == 9 and x["fee_paid"]]

percent = [round(x["marks"]/150*100,1) for x in students]

print(high)
print(result)
print(fee_paid)
print(percent)