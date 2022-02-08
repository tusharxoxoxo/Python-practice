# in this lecture we will learn adding a removing items
letters = [1, 2, 3]
letters.append(4)
print(letters)
letters.append("a")
print(letters)
letters.insert(0, "-")
letters.insert(4, "---")
print(letters)
letters.pop()
print(letters)
letters.pop(4)
print(letters)
letters.remove("-")
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)

