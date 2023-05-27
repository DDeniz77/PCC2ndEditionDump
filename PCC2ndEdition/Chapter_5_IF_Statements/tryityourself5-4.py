# 5-4. Alien Colors #2:
alien_color = 'red'
points = 0
if 'green' in alien_color:
    points = (points + 5)
    print(f"You just earned 5 points, your new total is {points} points")
if 'green' not in alien_color:
    points = (points + 10)
    print(f"You just earned 10 points, your new total is {points} points")
# Same code with else instead of if.
alien_color = 'red'
points = 0
if 'green' in alien_color:
    points = (points + 5)
    print(f"You just earned 5 points, your new total is {points} points")
else:
    points = (points + 10)
    print(f"You just earned 10 points, your new total is {points} points")
