# 6-11. Cities:
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_000_000,
        'became_capital': 1868,
    },
    'ankara': {
        'country': 'turkey',
        'population': 5_000_000,
        'became_capital': 1923,
    },
    'london': {
        'country': 'england',
        'population': 9_000_000,
        'became_capital': 1066,
    },
}
for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    capital = info['became_capital']
    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of about {population}.")
    print(f"It became a capital in {capital}.")
