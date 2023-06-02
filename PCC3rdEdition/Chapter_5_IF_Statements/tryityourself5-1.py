# 5-1. Conditional Tests
car = 'subaru'
print(f"Is your car a Subaru?, I predict True.")
print(car == 'subaru')

print("\nIs your car an Audi? I predict False.")
print(car == 'audi')
print(car == 'toyota')

fav_food = 'pizza'
print("Is your favorite food pizza?")
if fav_food == 'pizza':
    print(f"Yes {fav_food} is my favorite\n")
else:
    print(f"Nope, pizza is not my favorite, it is {fav_food}\n")

guess_fav_food = 'meatloaf'
print(f"Is your favorite food {guess_fav_food}?")
real_fav_food = 'fish & chips'
if guess_fav_food == fav_food:
    print(f"Yes {fav_food} is my favorite")
else:
    print(f"Nope, {guess_fav_food} is not my favorite, it is {real_fav_food}.")
