# However, sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 would not work as tuples are not changeable
# Tuples are technically defined by the presence of a comma; the parentheses make them
# look neater and more readable. If you want to define a tuple with one element, you
# need to include a trailing comma:
my_t = (3,)
# It does not often make sense to build a tuple with one element, but this can happen
# when tuples are generated automatically.
print(my_t[0])
print(my_t)
# You can loop over all the values in a tuple using a for loop, just as you did with a list:
for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout the life of a program.
