# 5-5. Alien Colors #3:
alien_color = 'red'
points = 0
if 'green' in alien_color:
    points = (points + 5)
    print(f"You just earned 5 points, your new total is {points} points")
elif alien_color == 'yellow':  # using == instead of in
    points = (points + 10)
    print(f"You just earned 10 points, your new total is {points} points")
else:
    points = (points + 15)
    print(f"You just earned 15 points, your new total is {points} points")