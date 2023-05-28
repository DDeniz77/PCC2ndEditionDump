# 4-10. Slices:
my_foods = ["pizza", "falafel", "carrot cake", "kebab", "baklava"]
print("First the items of the list are ")
for foods in my_foods[:3]:
    print(foods.title())
print("\nItems in the middle of the list are ")
for foods in my_foods[1:4]:
    print(foods.title())
print("\nLast three items of the list are ")
for foods in my_foods[-3:]:
    print(foods.title())

# List comprehension alternative
cubes = [num**3 for num in range(1, 11)]
# print(cubes)
print(f"First 3 cubed numbers are {cubes[:3]}")
# Just eyeballing for the middle numbers for now
print(f"Cubed numbers in the middle of my list are {cubes[4:-4]}")
print(f"Last 3 cubed numbers are {cubes[-3:]}")
