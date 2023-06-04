# 5-11. Ordinal Numbers:
numbers = []
i = 0
while i < 9:
    i = i + 1
    numbers.append(i)
    if i == 0:
        break
print(numbers)
print(i)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(str(number)+"th")
#   else:
#       print(f"{number}th")
