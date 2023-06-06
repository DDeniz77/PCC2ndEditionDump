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
