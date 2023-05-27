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
