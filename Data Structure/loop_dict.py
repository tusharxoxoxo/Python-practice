point = dict(x = 1, y = 2, z = 3)
print(point)

for x in point:
    print(x)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)
#in the above case we are getting tuple as output

# now we will unpack out tuple

for key, value in point.items():
    print(key, value)

