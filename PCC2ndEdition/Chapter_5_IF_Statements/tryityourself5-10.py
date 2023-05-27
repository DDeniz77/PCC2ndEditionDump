# 5-10. Checking Usernames:
current_users = ["levent", "fikret", "ozan", "yunus", "admin"]
new_users = ["FIKRET", "Levent", "hasan", "metin", "çetin"]
new_users_lower = [new_user.lower() for new_user in new_users]
for nulower in new_users_lower:
    if nulower in current_users:
        print(f"Sorry {nulower}, you need to enter a new username")
    else:
        print(f"The username {nulower} is available")

# checking usernames without list comprehensions
# You should be converting Turkish İ to I so that Phyton doesn't fuck up
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
