# 7-2. Restaurant Seating:
party_seating = input("How many seats will you reserve? ")
party_seating = int(party_seating)
if party_seating > 8:
    print("Unfortunately you will have to wait for a table.")
else:
    print("Your table is ready")
