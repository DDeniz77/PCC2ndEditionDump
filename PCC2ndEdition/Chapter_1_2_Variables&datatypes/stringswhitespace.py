print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript") 
#stripping whitespace to see if both lines are the same space vs spacespace example
#Python can look for extra whitespace on the right and left sides of a
#string. To ensure that no whitespace exists at the right end of a string, 
#use the rstrip() method.
favorite_language = '   python '
print (favorite_language) 
print (favorite_language.rstrip()) #this strips the right side use lstrip() for left side
print (favorite_language.lstrip())
print (favorite_language.lstrip().rstrip()) #you can chain these
print (favorite_language.strip()) #simply use these for stripping both sides
