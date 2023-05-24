#2.3

name = "Darkness"
hey = f"Hello {name} my old friend, I have come to talk to you again"
print (hey)

#2.3 cleaner
print (f"Hello {name} my old friend, I have come to talk to you again")

#2.4
print (f"{name.title()}\n{name.lower()}\n{name.upper()}\n")

#2.5 and #2.6 use \" \" for quotes

quote = "\"A person who never made a mistake never tried anything new.\""
author = "Albert wifebeater Einstein"
print (f"{author} once said, {quote}")

#2.7
specimen = "   Albert wifebeater Einstein   "
print (specimen)
print (f"{specimen.lstrip()}\n{specimen.rstrip()}\n{specimen.strip()}")
