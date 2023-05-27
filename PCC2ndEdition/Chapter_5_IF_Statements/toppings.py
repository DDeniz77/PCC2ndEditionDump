requested_topping = "mushrooms"
if requested_topping != "anchovies":  # this is a weird example!?
    print("Hold the anchovies!")

requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print(f"{requested_toppings[0].title()} is requested as a topping")
if "pepperoni" in requested_toppings:
    print("Pepperoni is requested as a topping")
else:
    print("Pepperoni is not requested as a topping")
# Maybe I should add a line that retrieves "mushrooms" from the list?

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")