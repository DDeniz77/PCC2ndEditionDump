# 5-2. More Conditional Tests
name = "ADA lovelace"
expected = "ada lovelace"
if expected == name:
    print("The names are equal.")
else:
    print("The names are not equal.")
if expected == name.lower():
    print("They are the same name with case difference.")
number = 5
mynumber = 9
if number == mynumber:
    print(f"{number} equals {mynumber}")
if number < mynumber:
    print(f"{number} is lower than {mynumber} ")
if number > mynumber:
    print(f"{number} is greater than {mynumber} ")

for value in range(6):
    print(f"{value}")
    if value == 1:
        print(f"1 is a part of the value")
    if value == 1:
        break

age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print(True)
else:
    print(False)

my_list = ["hi", "hello", "darkness"]
if "darkness" in my_list:
    print("darkness is part of the list")
if "pizzeria" not in my_list:
    print("pizzeria is not a part of the list")
