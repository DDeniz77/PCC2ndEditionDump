squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)  # Filling the list with values(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
print(f"sum of all the squares is {sum(squares)} with the first square being "
      f"{squares[0]} and the final square being {squares[-1]}")
# A list comprehension combines the for loop and the creation of new
# elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1, 12)]
print(squares)
print(f"sum of all the squares is {sum(squares)} with the first square being "
      f"{squares[0]} and the final square being {squares[-1]}")