# Sorting a List Permanently with the sort() Method
# sorts the list in alphabetical (or in reverse) order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
# The sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\nHere is the sorted list in reverse alphabetical order:")
print(sorted(cars, reverse=True))  # True has to be title case!

# Sorting a list alphabetically is a bit more complicated when all the values
# are not in lowercase. There are several ways to interpret capital letters
# when determining a sort order

# printing a list in reverse order (doesn't "sort" alphabetically it just
# reverses the order of input)
print("\n\n\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# The reverse() method changes the order of a list permanently, but you can
# revert to the original order anytime by applying reverse() to the same
# list a second time.

# Finding the length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# Python counts the items in a list starting with one, so you shouldn’t run into
# any off by-one errors when determining the length of a list.
# You’ll find len() useful when you need to identify the number of aliens that
# still need to be shot down in a game, determine the amount of data you have to
# manage in a visualization, or figure out the number of registered users on a
# website, among other tasks.
