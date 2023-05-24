squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)  # Filling the list with values(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
# A list comprehension combines the
# for loop and the creation of new elements into one line, and automatically
# appends each new element.
squares = [value**2 for value in range(1, 11)]
print(squares)
