from pprint import pprint
sentence = "This is a common interview question"

frequency = {}
for char in sentence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)      
pprint(frequency, width = 1)
print("\n\n")
answer = sorted(frequency.items(), key = lambda j:j[1], reverse = True)
print(answer[0])

