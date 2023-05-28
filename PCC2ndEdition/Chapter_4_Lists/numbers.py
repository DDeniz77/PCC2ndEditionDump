for value in range(1, 5):
    print(value)  # Doesn't print 5 due to the off-by-one nature of most
    # programming languages.
for value in range(6):
    print(f"value is {value}")

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
odd_numbers = list(range(1, 11, 2))  # 2 by 2
print(odd_numbers)
