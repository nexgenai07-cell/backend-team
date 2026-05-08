#Input marks in 3 subjects
math = int(input("Math marks: "))
science = int(input("Science marks: "))
english = int(input("English marks: "))
total = math + science + english

# Print formatted result card
print(f"\n{'Subject':<12} {'Marks':<6}")
print("-" * 20)
print(f"{'Math':<12} {math:>6}")
print(f"{'Science':<12} {science:>6}")
print(f"{'English':<12} {english:>6}")
print("-" * 20)
print(f"{'Total':<12} {total:>6}")