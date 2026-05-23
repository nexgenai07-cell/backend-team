students = [
    {"name": "Ali Hassan", "class": "9B", "marks": 88, "fee_paid": True, "attendance": 80},
    {"name": "Kamil Baig", "class": "9B", "marks": 97, "fee_paid": True, "attendance": 92},
    {"name": "Zara Siddiq", "class": "10", "marks": 41, "fee_paid": False, "attendance": 70},
    {"name": "Sara Malik", "class": "8A", "marks": 67, "fee_paid": True, "attendance": 76}
]

topper = students[0]
lowest = students[0]

for s in students:
    if s["marks"] > topper["marks"]:
        topper = s

    if s["marks"] < lowest["marks"]:
        lowest = s

print("Topper:", topper["name"])
print("Lowest:", lowest["name"])

count = {}
for s in students:
    cls = s["class"]
    count[cls] = count.get(cls, 0) + 1

print(count)

for s in students:
    if s["attendance"] >= 75 and s["fee_paid"]:
        print("Eligible:", s["name"])

search = input("Search name: ").lower()

for s in students:
    if search in s["name"].lower():
        print("Found:", s["name"])

total = {}
num = {}

for s in students:
    cls = s["class"]

    total[cls] = total.get(cls, 0) + s["marks"]
    num[cls] = num.get(cls, 0) + 1

for cls in total:
    print(cls, "Average =", total[cls] / num[cls])