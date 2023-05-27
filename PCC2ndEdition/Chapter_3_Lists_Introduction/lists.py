bicycles = ["trek", "cannondale", "redline", "specialized"]
print (bicycles)

#If you ask Python to print a list, Python returns its representation of the
#list, including the square brackets:
#Because this isn’t the output you want your users to see, let’s learn how
#to access the individual items in a list. 

print (bicycles[0],bicycles[2],bicycles[2].title())
print (bicycles[-1]) #-1 returns the last item on any list
print (bicycles[-2]) #-2 returns the second last item on any list and so on..

message = f"My first bicycle was a {bicycles[0].title()}."
print (message)