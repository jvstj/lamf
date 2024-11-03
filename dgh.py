# import random
# print( random.randrange(000000,999999))
import math
while True:
    number=int(input("Enter a number: "))
    result= math.factorial(number)
    print(f"The factorial of {number} is {result}")
    quit="if you want to quit press 'y'"
    print(quit)
    if quit.lower() == 'y':
        break


