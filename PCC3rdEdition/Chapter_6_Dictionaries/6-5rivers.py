# 6-5. Rivers:
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
    'yangtze': 'china',
    'yellow': 'china',
}
for river, country in rivers.items():
    print(river.title() + " runs through " + country.title())
    print(river)
    print(country)
# bonus set example:
countries = rivers.values()
for country in set(countries):
    print(country)
