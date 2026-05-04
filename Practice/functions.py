import random
def max_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
            print(f"The minimum is: {minimum}")
    return minimum
def getValues():
    list = random.sample(range(50,100),10)
    print(list)
    max_min(list)

getValues()
