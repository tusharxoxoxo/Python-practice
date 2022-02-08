# list vs array
# array takes less memory and are faster than list


from array import array 

numbers = array("i", [1, 2, 3])

print(numbers)

numbers.insert(4, 0)
print(numbers)
numbers.append(4)
print(numbers)

