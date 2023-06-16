# 7-3. Multiples of Ten:
number = input("Please enter a number to check if it's a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")
