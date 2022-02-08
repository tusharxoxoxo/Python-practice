course = "Programming \" Skills"
print(course)
# here in this case we have used \ as an escape sequence
# " symbol after our escape sequence is skipped or unseen 
course = "Programming \' Skills"
print(course)
course = "Programming \\ Skills"
print(course)
course = "Programming \n Skills"
print(course)

first = "Tushar"
last = "Dahiya"
full = first + " " + last 
print(full)
#another way of doing the exace same thing
#formatter strings 
full2 = f"{first} {last}"
print(full2)

joy = "   Lundureh   saleh   "
print(joy.upper())
print(joy) #original string is still the same
print(joy.lower())
print(joy.title())
#if user has written couple of white spaces at the input
print(joy.strip())
print(joy.rstrip())
print(joy.lstrip())
print(joy.find("sa"))
print(joy.find("Sa"))
print(joy.replace("u","s"))
#difference between find and in find returns the index but in returns boolean
print("Lun" in joy)
print("swift" not in joy)
print("fucking si good enough")
