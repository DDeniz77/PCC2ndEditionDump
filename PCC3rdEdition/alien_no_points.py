alien_0 = {'color': 'green', 'speed': 'slow'}
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key does not exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If the key 'points' exists in the dictionary, you’ll get the corresponding
# value. If it does not, you get the default value. In this case, points
# does not exist, and we get a clean message instead of an error:
point_value = alien_0.get('points')
print(point_value)
# If you leave out the second argument in the call to get() and the key does not
# exist, Python will return the value None. The special value None means
# “no value exists.” This is not an error: it’s a special value meant to
# indicate the absence of a value. You’ll see more uses for None in Chapter 8.
