# 5-8. Hello Admin:
names = ["levent", "fikret", "ozan", "yunus", "admin"]
for name in names:
    if name == "admin":
        print(f"Hello {name.title()}, would you like to see the status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")