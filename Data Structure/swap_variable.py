# classic way of swapping 

x = 10
y = 11

z = x 
x = y
y = z 

print("x", x)
print("y", y)

# a better way of doing the same is using python built in function

x, y = y, x  # this a tuple x, y = (11, 10)
# in this we are defining a tuple and then unpackign it on the left hand side

print("x", x)
print("y", y)

