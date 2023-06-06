alien_0 = {'color': 'green', 'speed': 'slow'}
# The get() method requires a key as a first argument. AS A SECOND OPTIONAL
# ARGUMENT, YOU CAN PASS THE VALUE TO BE RETURNED IF THE KEY DOES NOT EXIST
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If the key 'points' exists in the dictionary, you will get the corresponding
# value. If it does not, you get the default value. In this case, points
# does not exist, and we get a clean message instead of an error:
point_value = alien_0.get('points')
print(point_value)
# If you leave out the second argument in the call to get() and the key does not
# exist, Python will return the value None. The special value None means
# “no value exists.”
point_value = alien_0.get('randomkey', 'absence_of_key')
print(point_value)
# There is no key called 'randomkey' so we get the second argument 'absence'
# get() is used to avoid traceback errors and return an optional argument.
