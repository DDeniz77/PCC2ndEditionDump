# 5-10. Checking Usernames:
current_users = ["levEnt", "fiKret", "Ozan", "yunus", "admin"]
current_users_lower = [users.lower() for users in current_users]  # IT WORKS
print(current_users_lower)
new_users = ["FIKRET", "Levent", "hasan", "metin", "çetin"]
new_users_lower = [new_user.lower() for new_user in new_users]  # IT WORKS
# We keep assigning different name for the same object
for nulower in new_users_lower:
    if nulower in current_users_lower:
        print(f"Sorry {nulower}, you need to enter a new username")
    else:
        print(f"The username {nulower} is available")

# Checking usernames without list comprehensions
# You should be converting Turkish 'İ' to 'I'!
current_users = ["admiral", "general", "levent", "deniz", "erdem"]
new_users = ["GENERAL", "daniel", "derya", "DENIZ"]
new_users_lower = []
for users in new_users:
    new_users_lower.append(users.lower())
for nusersl in new_users_lower:
    if nusersl in current_users:
        print(f"The name {nusersl} is taken")
    else:
        print(f"The name {nusersl} is not taken")
# Note that this only accounts for current users being in lowercase
