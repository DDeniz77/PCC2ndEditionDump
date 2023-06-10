# 6-8. Pets:
pet1 = {
    'species': 'alligator',
    'owner': 'floridan',
    'weight': '45',
    'age': '30',
}
pet2 = {
    'species': 'moose',
    'owner': 'canadian',
    'weight': '145',
    'age': '22',
}
pet3 = {
    'species': 'mice',
    'owner': 'newyorker',
    'weight': '1',
    'age': '5',
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"\nLet's talk about {pet['species']}")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

# alternatively you can create an empty list called pets and append each pet
# named simply as pet one by one.
