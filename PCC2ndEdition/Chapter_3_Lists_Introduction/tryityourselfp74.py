#3.1

allmyfriends = ["darkness", "cthulu", "righthand", "lefthand"]
print (allmyfriends[0],allmyfriends[1],allmyfriends[2],allmyfriends[3])

#3.2 without the need to define the message can be done by str function
#and many other ways but for now we will use this simple way.

greet = f"hello {allmyfriends[0].title()}\n" \
        f"Hello {allmyfriends[1].title()}\n" \
        f"Hello {allmyfriends[2].title()}\nHello {allmyfriends[3].title()}\n "

print (greet)
 

#3.3

transport = ["Car", "Train", "Plane", "Scooter","Bicycle"]

transport_message = f"I would like to get to work by {transport[1].lower()}" \
                    f", if it is crowded a {transport[0].lower()} is fine too"
print (transport_message)