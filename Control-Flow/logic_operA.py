high_income = True
low_income = False

if high_income == True and low_income == False:
    print("u little bitch ")
#above code is noob kind of code

#bettter way
if high_income and low_income:
    print("u little bitch")
#high_income and low_income are already boolean so we don't need to compare it with == True and == False


# age between 18 and 65

age = 45

if age > 10 and age <65:
    print("Eligible")

#another way of same thing

message = "Eligible" if age > 18 and age < 65 else "Not Eligible"
print(message)


if 18 <= age < 65 :
    print("Eligible")
else :
    print("Not Eligible")

 

