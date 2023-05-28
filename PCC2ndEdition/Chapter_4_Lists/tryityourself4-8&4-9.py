# 4-8 Cubes
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:  # assign a name to the values
    print(cube)

# Maybe an irrelevant way
for cubes in range(1, 11):
    print(cubes**3)

# 4-9. Cube Comprehension
cubes = [num**3 for num in range(1, 11)]
print(cubes)
for cube in cubes:  # assign a name to the values
    print(cube)
