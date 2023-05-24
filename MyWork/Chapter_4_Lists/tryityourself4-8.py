# 4-8. Cubes
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# Maybe an irrelevant way
for cubes in range(1,11):
    print(cubes**3)