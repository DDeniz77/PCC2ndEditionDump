#Numbers Mason! What do they mean?

print (2+3)
print (3-2)
print (2*3)
print (3/2)

print (3**2)
print (2**3)
print (3**3)

print (6**10) #6 to the power of 10
print (10**6) #10 to the power of 6

print (2+3*4) #python supports order of operations
print ((2+3)*4)
print (( 2 + 3 ) * 4) #spacing has no effect on how python evaluates the expressions

print (0.1+0.1)
print (0.2+0.2)
print (2*0.1)
print (2*0.2)
print (0.2+0.1) #Do not mind small decimal rounding errors for now
print (3*0.1)
# When you divide any two numbers, even if they are integers that result in a 
# whole number, you’ll always get a float
print (4/2)
# If you mix an integer and a float in any other operation, you’ll get a
# float as well
print (1+2.0)
print (2*3.0)
print (3.0**2) 
# Python defaults to a float in any operation that uses a float, even if the
# output is a whole number. 

universe_age = 14_000_000_000 # '_' makes it easier to read
print (universe_age)

universe_age_alternate = "14.000_000_000" #output defined as is.
print (universe_age_alternate)

x, y, z = 0, 1, 2
print (x,y,z) #You need to separate the variable names with commas

#Python doesn’t have built- in constant types, 
#but Python programmers use all capital letters to indicate a variable
#should be treated as a constant and never be changed:

MAX_CONNECTIONS = 5000
print (MAX_CONNECTIONS)

MAX_CONNECTIONS = 4000
print (MAX_CONNECTIONS)