def greet():
    print("Hi there")
    print("Welcome Aboard")

greet()

def gool(first_name, second_name):
    print(f"Hi {first_name} {second_name} ")
    print("Welcome Aboard")

gool("Tushar", "Dahiya")
gool("Pussy", "Cunt")
# there are two types of functions
# first Which calculate a value
# which return a value 

def fool(first_name):
    return f"Hi {first_name}"

message = fool("Tushar")
print(message)
print(fool("Tushar"))

print(gool("Tushar", "Dahiya"))


#manipulation with files
message = fool("Tushar")
file = open("context.txt", "w")
file.write(message)
