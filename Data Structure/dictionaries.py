# first way of using dictionary in python
point = {"x": 1, "y": 2}

# the second way of using dictionary in python
pointing = dict(x = 1, y = 2)
# we can't get values out of dictionary by using index such as pointing[0] will not give us output
# a dict contains a key and a value so we can access values in dict by key
print(point["x"])
print(pointing["y"])
 # similarly we can change it's value to any value 
pointing["y"] = 10
print(pointing["y"])
pointing["z"] = 20
print(pointing)
# if we input the wrong key then it will output as wrong key
# better way is to first test wheather it is present or not
if "a" in point:
    print(point["a"])
point["a"] = 40
if "a" in point:
    print(point["a"])

# similiar thing can be done using get method 
print(point.get("b")) # the output will be none if that key is not present 
# we can also change the output
print(point.get("b", 0))
print(point.get("x", 8999))
del point["x"]
print(point)

