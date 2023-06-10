# nesting example:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]  # dictionaries nested in a list
for alien in aliens:
    print(alien)

# using range() to create a fleet of aliens:
aliens = []
for alien_number in range(30):  # just tells the amount of times we want to loop
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)  # adds 30 of new_alien to the aliens list
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}")

# modify some aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':  # make sure these are the aliens you want
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
