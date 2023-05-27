# Changing, Adding, and Removing Elements

# To change an element, use the name of the list followed
# by the index of the element you want to change, and then provide the new
# value you want that item to have.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')  # append adds element to the end
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')  # shifts every other value on the list to the right
print(motorcycles)

# removing an item using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]  # rip honda
print(motorcycles)
del motorcycles[1]  # rip suzuki
print(motorcycles)
# You can no longer access the values that were removed by using del statement


# removing an item using the pop() method
# The pop() method removes the last item in a list, but it lets you work
# with that item after removing it. The term pop comes from thinking of a
# list as a stack of items and popping one item off the top of the stack. In
# this analogy, the top of a stack corresponds to the end of a list.
print("pop example starts here")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()  # pops the last item in the list
print(motorcycles)
print(popped_motorcycle)

# Imagine that the motorcycles in the list are stored in
# chronological order according to when we owned them.
# If this is the case, we can use the pop() method to print a statement
# about the last motorcycle we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print("\n\n\n\n\n\n")

# popping items from any position in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# If we do this again we would get an index error as there are no more
# items on the list

# Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove, you
# can use the remove() method.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that’s being
# removed from a list. Let’s remove the value 'ducati' and print a reason for
# removing it from the list;

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive.title()} is too expensive for me")

# The remove() method deletes only the first occurrence of the value you
# specify. If there’s a possibility the value appears more than once in the
# list, you’ll need to use a loop to make sure all occurrences of the value are
# removed. You’ll learn how to do this in Chapter 7.
