# 5-9. No Users:
names = []
if names == []:  # you can use "if not names" instead.
    print("We need to find some users!")
for name in names:
    if name == "admin":
        print(f"Hello {name.title()}, would you like to see the status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")

# ehmatthes way to do this

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")
