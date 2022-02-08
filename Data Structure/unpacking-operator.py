numbers = [1, 2, 3]
print(numbers)
print(*numbers)
values = print(list(range(10)))

falues = [range(10)]
print(falues)

jalues = [*range(10)]
print(jalues)

kalues = print([*range(10), *"Hello"])

# using unpacking operator we can combine lists
print("\n\n")
first = [1, 2, 3]
second = [4, 5, 6]
third = print(first + second)

nalues = [*first, *second]
print(nalues)
salues = [*first, "a", *second, "Hello", *"Gello"]
print(salues)


# using unpacking on dictionaries 

print("\n\n")
third = {"d": 56}
fourth = {"e": 65, "f": 33}
fifth = {**third, "g": 56, **fourth}
print(fifth)
# if u have multiple values with same key then last value will be used 

