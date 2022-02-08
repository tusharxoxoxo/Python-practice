# making optional functions giving us freedom to input optional parameter or not
 # optional parameter must come after required parameter
# we can do this by assigning a default value to parameter

def increment(number = 45, by = 1):
    return number + by

print(increment())

