items = [
        ("Product1", 100),
        ("Product2", 34324),
        ("Product3", 5555)
        ]

x = filter(lambda item:item[1] >= 30, items)
print(x)
y = print(filter(lambda item:item[1] >= 30, items))
z = print(list(filter(lambda item:item[1] >= 300, items)))

