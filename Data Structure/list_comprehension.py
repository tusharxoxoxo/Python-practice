items = [
        ("Product1", 2343),
        ("Product2", 23455),
        ("Product3", 665)
        ]

filter = [item[1] for item in items]
print(filter)

filtered = [item for item in items if item[1] >= 1000]
print(filtered)

