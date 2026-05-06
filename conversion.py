fee_str = "15000"
fee_int = int(fee_str)
fee_float = float(fee_int)

tax = fee_float * 0.05
final = fee_float + tax

print("Final Fee with Tax: ", final)