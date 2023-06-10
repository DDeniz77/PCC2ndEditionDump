# 6-3. Glossary:
glossary = {
    'list': 'stores data',
    'del': 'delete function',
    'pop': 'pops an item from a list',
    'truefalse': 'conditional tests',
    'nesting': 'programming construct included within another',
 }
word = 'list'
print(f"{word.title()}: {glossary[word]}")
word = 'del'
print(f"{word.title()}: {glossary[word]}")
word = 'pop'
print(f"{word.title()}: {glossary[word]}")
word = 'truefalse'
print(f"{word.title()}: {glossary[word]}")
word = 'nesting'
print(f"{word.title()}: {glossary[word]}")

# looping version:
glossary = {
    'list': 'stores data',
    'del': 'delete function',
    'pop': 'pops an item from a list',
    'truefalse': 'conditional tests',
    'nesting': 'programming construct included within another',
 }
for key, value in glossary.items():
    print(f"{key}: {value}")

print("\n\n")
# 6-4 Glossary 2
glossary['loop'] = 'Work through a collection of items, one at a time.'
for key, value in glossary.items():
    print(f"{key}: {value}")
