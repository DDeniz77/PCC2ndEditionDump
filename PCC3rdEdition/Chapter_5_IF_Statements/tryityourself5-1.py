# 5-1. Conditional Tests
car = 'subaru'
print("Is car == 'subaru'?, I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print(car == 'toyota')

fav_food = 'pizza'
print("Is your favorite food pizza?")
print(fav_food == 'pizza')
if fav_food == 'pizza':
    print(f"Yes {fav_food} is my favorite")
else:
    print("Nope, pizza is not my favorite")

guess_fav_food = 'meatloaf'
print(f"Is your favorite food {guess_fav_food}?")
real_fav_food = 'fish & chips'
if guess_fav_food == fav_food:
    print(f"Yes {fav_food} is my favorite")
else:
    print(f"Nope, {guess_fav_food} is not my favorite, it is {real_fav_food}.")
