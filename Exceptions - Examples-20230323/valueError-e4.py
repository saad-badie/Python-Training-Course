try:
    # input number
    inputNumber = int(input("Enter Your Number: " )) 

except ValueError:
    print("Only integer value Accepted ")

else:
    # getting the square of a number 
    square = inputNumber * inputNumber
    # printing the square of a number
    print("The square of", inputNumber, "=", square)  
    