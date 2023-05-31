my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]  # Starts from first item, ends with the last item
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
# Basically, if you’re trying to work with a copy of a list, and you see
# unexpected behavior, make sure you are copying the list using a slice, as we
# did in the first example.
