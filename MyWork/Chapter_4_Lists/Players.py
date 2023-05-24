players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])  # Without a starting index, Python starts at the beginning of the list:
print(players[2:])
print(players[-3:])
print(players[:-3])
# You can include a third value in the brackets indicating a slice. If a third value is
# included, this tells Python how many items to skip between items in the specified
# range.
print(players[0:5:2])
print("Here are the first 3 players in my team:")
for player in players[:3]:
    print(player.title())