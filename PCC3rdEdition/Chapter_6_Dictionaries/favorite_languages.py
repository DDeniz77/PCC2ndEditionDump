favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
# When you know you’ll need more than one line to
# define a dictionary, press ENTER after the opening brace. Then indent the
# next line one level (four spaces), and write the first key-value pair,
# followed by a comma. From this point forward when you press ENTER,
# your text editor should automatically indent all subsequent key-value pairs
# to match the first key-value pair.
# Once you’ve finished defining the dictionary, add a closing brace on a
# new line after the last key-value pair and indent it one level so it
# aligns with the keys in the dictionary. It’s good practice to include a comma
# after the last key-value pair as well, so you’re ready to add a new key-value
# pair on the next line.
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# To see which language Sarah chose, we ask for the value at
# favorite_languages['sarah']
