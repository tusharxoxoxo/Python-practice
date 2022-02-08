# comprehension 
# [expression for item in items]

values = []
for x in range(5):
    values.append(x * 2)
print(values)

# same can be done using comprehension

vace = print([x * 2 for x in range(5)])

# same thing can be done in sets 

race = print({x * 2 for x in range(5)})

# for dict comprehension

face = print({x: x * 2 for x in range(5)})

# old way of doing same in dict 

ace = {}
for x in range(5):
    ace[x] = x * 2
print(ace)

# using comprehension for tuple

sace = print((x * 2 for x in range(5)))
# something strange we didn't get output but a generator operator
