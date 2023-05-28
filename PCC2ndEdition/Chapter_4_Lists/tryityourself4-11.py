# 4-11. My Pizzas, Your Pizzas:
pizzas = ["pepperoni", "marios", "italian"]
friend_pizzas = pizzas[:]

pizzas.append("mozzarella")
friend_pizzas.append("pineapple")

print(f"The pizzas I like are")
for pizza in pizzas:
    print("- " + pizza + " yo")  # option 1
print("\nMy friends pizzas are")
for f_pizza in friend_pizzas:
    print("- ", f_pizza)  # option 2
