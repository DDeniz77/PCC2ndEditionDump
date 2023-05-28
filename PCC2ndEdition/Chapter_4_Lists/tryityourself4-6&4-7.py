# 4-6. Odd Numbers
for numbers in range(1, 21, 2):
    print(numbers)

# 4-7. Threes
for numbers in range(3, 31, 3):
    print(numbers)
# 4-7 alternative (divisibility with 3)
for number in range(1, 31):
    if number % 3 == 0:
        print(number)
