letters = ["a", "b", "c", 1, 2, 3]
for letter in letters:
    print(letter)
# if we also want the item number in front of it
print("\n\n")
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("\n\n")
item = [0, "a"]
index, letter = item

for index, letter in enumerate(letters):
    print(index, letter)
