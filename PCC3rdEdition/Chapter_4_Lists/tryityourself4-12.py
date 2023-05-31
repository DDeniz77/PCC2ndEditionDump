# 4-12. More Loops:
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("My favorite foods are:")
for foods in my_foods:
    print("- " + foods.title())
print("My friend's favorite foods are:")
for foods in friend_foods:
    print("+ " + foods.title())

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for foods in my_foods:
    print(foods.title())
print("My friend's favorite foods are:")
for foods in friend_foods:
    print(foods.title())
# As you can see the variable "foods" in for loop can be the same for all loops
# since it is not a fixed value but instead given a value during the looping
# process
