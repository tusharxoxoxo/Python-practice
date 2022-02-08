#tuple is a read only list
# contains a sequence of object but we can't modify the sequence, 
# we can't add an object we can't remove an object 
# we can't modify an existign object
point = 1, 2
print(type(point))
points = (1, 2)
print(type(points))
pointss = 1
print(type(pointss))
pointsss = 1,       #if we add  a trailing comma to it then python will treat it as a tuple
print(type(pointsss))
# if we want to define an empty tuple then we need ()
pointssss = ()
print(type(pointssss))

joint = (1, 2) + (3, 4)
print(joint)
joints = (1, 2) * 5
print(joints)
# we can also convert  A LIst in tuple 

jointss = tuple([1, 2])
print(type(jointss))
print(jointss)

reflex = tuple("Hello World")
print(reflex)
print(type(reflex))

job = (1, 2, 3, 4, 5, 6)
print(job[1])
print(job[0])
print(job[0:2])

if 4 in job:
    print("Exitst")



