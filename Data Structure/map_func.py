items = [
        ("Product1", 3434),
        ("Product2", 343455),
        ("Product3", 3)
        ]

prices = []

for item in items:
    prices.append(item[1])

print(prices)

# but there is a more elegant way of achieving the exact same thing by usign map function

itemss = [
        ("Product4", 324),
        ("Product5", 324324),
        ("Product6", 3466)
        ]

x = map(lambda jar: jar[1], itemss)
print(x)
for jar in x:
    print(jar)

pricess = print(list(map(lambda jar: jar[1], itemss)))
