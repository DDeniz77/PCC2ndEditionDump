cars = ["audi", "toyota", "bmw", "ford"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
car = "Audi"
if car == "audi":  # python is case-sensitive
    print("true")
else:
    print("false")
if car.lower() == "audi":  # it is now case-insensitive
    print("true")
