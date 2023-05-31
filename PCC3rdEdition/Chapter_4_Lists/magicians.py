magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)  # The space at the beginning is an indentation,
# it acts as a flow chart for the code.
# Using singular and plural names can help you identify whether a section of
# code is working with a single element from the list or the entire list.

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
