# 6-10. Favorite Numbers:
favorite_numbers = {
    'Jonathan': ['2', '17'],
    'Joseph': '6',
    'Josuke': ['18', '12'],
    'Giorno': '9',
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number(s):")
    for number in numbers:
        print(f"\t-{number}")
