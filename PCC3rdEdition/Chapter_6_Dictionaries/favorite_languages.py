favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
# When you know you’ll need more than one line to
# define a dictionary, press ENTER after the opening brace. It’s good practice
# to include a comma after the last key-value pair as well, so you’re ready
# to add a new key-value pair on the next line.

# Most editors have some functionality that helps you format extended lists and
# dictionaries in a similar manner to this example.

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# To see which language Sarah chose, we ask for the value at
# favorite_languages['sarah']

# looping for both keys and values
for name, language in favorite_languages.items():
    print(f"{name}: {language}")

# looping for keys only
for name in favorite_languages.keys():  # you can omit .keys() as looping
    # through keys is the default behaviour
    print(name)

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()  # bring key value from dict
    print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in favorite_languages.keys():  # check if 'erin' exists
        print("Erin, please take the poll!")

# Temporarily sorting the dictionary while printing
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n\n")
for language in set(favorite_languages.values()):
    print(language.title())  # each item in set is unique and non-repeating.

# You can build a set directly using braces and separating the elements
# with commas:
# languages = {'python', 'rust', 'python', 'c'}
# It’s easy to mistake sets for dictionaries. When you see braces but no
# key-value pairs, you’re probably looking at a set. Unlike lists
# and dictionaries, sets do not retain items in any specific order
