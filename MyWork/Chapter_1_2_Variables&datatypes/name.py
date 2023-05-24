name = "Ada LovElacE"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f means format without f you wouldn't
# get the desired output
print(full_name)
print (f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print (message)
full_nameoldpython = "{} {}".format(first_name.title(), last_name.title())
print (full_nameoldpython) #This was the way to do it before 3.6