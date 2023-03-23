import math
try:
    # input number
    inputNumber = int(input("Enter Your Number: " ))
    # getting the square root of a number using Math module
    squareRoot = math.sqrt(inputNumber)
    # printing the square root of a number
    print("The square root of", inputNumber, "=", squareRoot)   

except ValueError:
    print("You can not get take the square root of a negative number ")