# 6-2. Favorite Numbers:
favorite_numbers = {
    'Jonathan': '2',
    'Joseph': '6',
    'Josuke': '12',
    'Giorno': '9',
}
# We will use looping for this in the future.

# ematthes way below

num = favorite_numbers['Jonathan']
print(f"Jonathan's favorite number is {num}.")
num = favorite_numbers['Joseph']
print(f"Joseph's favorite number is {num}.")
num = favorite_numbers['Josuke']
print("Josuke's favorite number is " + str(num) + ".")
num = favorite_numbers['Giorno']
print("Giorno's favorite number is " + str(num) + ".")
# notice the difference between {num} and str(num)
