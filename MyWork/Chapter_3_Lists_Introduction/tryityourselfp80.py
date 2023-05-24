# 3-4 Guest list

invitelist = ("darkness", "my", "friend")
print(f"Hola {invitelist[0].title()}! Deniz invites you to his party house!")
print(f"Hola {invitelist[1].title()}! Deniz invites you to his party house!")
print(f"Hola {invitelist[2].title()}! Deniz invites you to his party house!")

# 3-5 Changing Guest List

esteemedguests = ["life", "body", "mind"]
guest_gone = esteemedguests.pop(0)
esteemedguests.insert(0, "sanity")
print(f"It seems that the esteemed {guest_gone.title()} "
      f"won't be able to make it, so we will be accompanied by"
      f" {esteemedguests[0].title()} in his stead")

# 3-6 More Guests

print("We have found a bigger table so we need more guests!")

esteemedguests.insert(0, "baratheon")
esteemedguests.insert(2, "stannis")
esteemedguests.append("mannis")
print(esteemedguests)
i = 0
while i < len(esteemedguests):
    print(f"Hola {esteemedguests[i]}! Deniz invites you to his party house!")
    i += 1
# you can use ctrl+click to find each time the variable was used
# or use shift+F6 to change(refactor) them all together
print("\n\n\n\n\n\n\n")


# 3-7 Shrinking Guest List
chump = len(esteemedguests)
print("It seems that we have only enough space for two")
while chump > 2:
    gone = esteemedguests.pop()
    print(f"Sorry {gone} we don't have enough space for you")
    chump = len(esteemedguests)
print(
    f"{esteemedguests[0].title()},"
    f" {esteemedguests[1].title()}, you guys are still invited")
del esteemedguests[0]
del esteemedguests[0]
print(esteemedguests)
