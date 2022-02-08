numbers = [1,2,3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
# but there is a better way of doing the exactly same thing

# by using list unpacking 

ek, doh, thin = numbers
# but there is a condition we must fullfill for using list unpacking 
# that is number of items on left must be equal to numbers of elements in our list
# or else it will give error
car = [2,3,4,5,6,7,8]
ekk , dohh, *others = car
print(ekk)
print(dohh)
print(others)
first ,*otherss, last = car
print(first, last)
print(otherss)

