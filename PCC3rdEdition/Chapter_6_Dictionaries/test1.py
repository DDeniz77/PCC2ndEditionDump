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
