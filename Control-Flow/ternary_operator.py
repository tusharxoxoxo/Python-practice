age = 20 
if age >=10:
    print("Your age is greater than 10")
elif age >=5:
    print("Your age is greater than 5")
else:
    print("Your age is less than who knows ")
#now here a better way of writing the above thing


message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
