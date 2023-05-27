# 4-5. Summing a Million
numbers = []
for number in range(1, 1_000_001):
    numbers.append(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# A simpler way is:

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))