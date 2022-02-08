numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique = set(numbers)
print(numbers)
print(unique)

print("\n\n")
second = {2334, 342342}
print(second)
second.add(3)
print(second)
second.add(3434)
print(second)
second.remove(3434)
print(second)
print(len(second))

print("\n\n")
print(unique | second)
print(unique & second)
print(unique - second)
print(unique ^ second)

