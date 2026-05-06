num = int(input("Enter number: " ))

print(f"\nMultiplication Table of {num}")
print("-" * 20)

for i in range(1, 11):
    print(f"{num} x {i:2} = {num*i:3}")