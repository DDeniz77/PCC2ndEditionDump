# 6-2. Favorite Numbers:
favorite_numbers = {
    'lucy': '3',
    'daniel': '2',
    'zeynep': '6',
 }
# for name in favorite_numbers: (how did this happen lmao)
#    for value in name:
#        print(value)

# print(f"Lucy's favorite number is {favorite_numbers['lucy']}")
# Maybe in the future I can do a loop for names and stuff.

# num = favorite_numbers['lucy']
# print(f"Lucy's favorite number is {num}.")

# ematthes way below

num = favorite_numbers['lucy']
print("Lucy's favorite number is " + str(num) + ".")
num = favorite_numbers['daniel']
print("Daniel's favorite number is " + str(num) + ".")
num = favorite_numbers['zeynep']
print("Zeynep's favorite number is " + str(num) + ".")