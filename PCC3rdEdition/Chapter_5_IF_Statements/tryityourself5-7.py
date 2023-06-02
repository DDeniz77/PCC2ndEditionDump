# 5-7. Favorite Fruit:
favorite_fruits = ['banana', 'tangerine', 'melon']
if 'banana' in favorite_fruits:
    print("You really like bananas")
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'melon' in favorite_fruits:
    print("You really like melons")
if 'pears' in favorite_fruits:
    print("You really like pears")
if 'tangerine' in favorite_fruits:
    print("You really like tangerines")

# Alternative for loop to print all
for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}s")
