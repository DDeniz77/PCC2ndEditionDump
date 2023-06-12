# 6-9. Favorite Places:
favorite_places = {
    'deniz': ['ankara', 'london', 'hokkaido'],
    'erin': ['hawaii', 'iceland'],
    'allie': ['mt. everest', 'the playground', 'new hampshire']
}
for person, places in favorite_places.items():
    print(f"\n{person.title()} likes:")
    for place in places:
        print(f"\t-{place.title()}")
