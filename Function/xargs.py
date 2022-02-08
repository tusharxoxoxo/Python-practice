def increment(*numbers):
    print(numbers)

def dance(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

increment(3,4,5,6)
print(dance(1,2,3,4,5,6))



