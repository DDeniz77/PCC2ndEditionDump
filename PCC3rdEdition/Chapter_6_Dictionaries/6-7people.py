# 6-7. People:
person1 = {
    'name': 'Slim',
    'surname': 'Shady',
    'age': '66',
    'city': 'NYC',
 }
person2 = {
    'name': 'John',
    'surname': 'Cena',
    'age': '52',
    'city': 'Beijing',
}
person3 = {
    'name': 'Michael',
    'surname': 'Jackson',
    'age': '40',
    'city': 'disco city',
}

people = [person1, person2, person3]
for person in people:
    print(f"The name is {person['name']} {person['surname']}")
    print(f"Age {person['age']} from {person['city']}")

# Ematthes way of doing it:
#    name = f"{person['first_name'].title()} {person['last_name'].title()}"
#    age = person['age']
#    city = person['city'].title()
#    print(f"{name}, of {city}, is {age} years old.")
