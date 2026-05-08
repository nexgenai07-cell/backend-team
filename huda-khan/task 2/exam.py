students = [
    {"name": "Ali Hassan", "fee_paid": True},
    {"name": "Sara Ahmed", "fee_paid": False},
    {"name": "Umar Khan", "fee_paid": True},
    {"name": "Bilal Raza", "fee_paid": True}
]

seat = 1

for s in students:

    if s["fee_paid"] == False:
        print(s["name"], "[BLOCKED]")
        continue

    if seat > 10:
        break

    print("Seat", seat, ":", s["name"])
    seat += 1