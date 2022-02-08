numbers = [1,234,545,656,0 , 0 ,43234]
numbers.sort()
print(numbers)
print(sorted(numbers, reverse = True))

print("\n\n")

items = [
        ("Product1", 3410),
        ("Product2", 20),
        ("Product3", 3434)
        ]
items.sort()
print(items)
print(sorted(items))
# in this case it's not getting sorted 

def sort_items(items):
    return items[1]

items.sort(key = sort_items)
print(items)

