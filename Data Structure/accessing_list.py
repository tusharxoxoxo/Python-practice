letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("[0]")
print(letters[0])
print("[-1]")
print(letters[-1])
# -1 will print last element of the list
# -2 will print second last element of the list
letters[0] = "A"
print("[0]")
print(letters[0])
print("letters")
print(letters)
print("[0:1]")
print(letters[0:1])
print("[0:6]")
print(letters[0:6])
print("[3:4]")
print(letters[3:4])
print("[:5]")
print(letters[:5])
#if we don't specify the first argument then zero 0 will be assumed at it's place
# similarly if end is not included then length of the list will be assumed 
print("[4:]")
print(letters[4:])
# if first and end argument is not given then entire list is assumed
print("[:]")
print(letters[:])
# we can also pass  a step 
print("[::3]")
print(letters[::3])
print("[::2]")
print(letters[::2])
print("[::5]")
print(letters[::5])
numbers = list(range(40))
print(numbers[::3])
# if we write ::-1 then it will print every element in list but in reverse order
print(numbers[::-1])

