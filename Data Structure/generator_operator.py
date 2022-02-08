from sys import getsizeof 
# they are iterable
#  and in each iteration they spit out a new value
# unlike a linked list they don't store every value but spit out a new value every time

# creating a list using a list comprehension operation

values = [x * 2 for x in range(5)]
for x in values:
    print(x)
# the above one is very memory inefficient
# doing exactly same in generator

print("\n\n")

vvalues = (x * 2 for x in range(5))
print(vvalues)
print(type(vvalues))
for x in vvalues:
    print(x)

print("\n\n\n")
print("list", getsizeof(values))
print("list", getsizeof(vvalues))
print("\n\n\n")
calues = [x * 3 for x in range(50000)]
ccalues = (x *3 for x in range(50000))
print("list", getsizeof(calues))
print("gen", getsizeof(ccalues))

