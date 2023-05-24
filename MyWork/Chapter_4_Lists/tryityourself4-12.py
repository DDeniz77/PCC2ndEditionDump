# 4-12. More Loops:
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("My favorite foods are:")
for mfoods in my_foods:
    print(mfoods.title())
print("My friend's favorite foods are:")
for ffoods in friend_foods:
    print(ffoods.title())

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for mfoods in my_foods:
    print(mfoods.title())
print("My friend's favorite foods are:")
for ffoods in friend_foods:
    print(ffoods.title())
