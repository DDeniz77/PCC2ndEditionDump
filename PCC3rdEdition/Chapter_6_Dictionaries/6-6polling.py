# 6-6. Polling:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
poll_people = ['jen', 'sarah', 'jonathan', 'aisha']
for people in poll_people:
    if people in favorite_languages.keys():
        print(f"{people.title()} thank you for responding.")
    else:
        print(f"{people.title()} you should take the poll!")
