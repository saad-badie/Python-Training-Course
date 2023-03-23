def main():
	x = get_number()
	square = x * x
	# printing the square root of a number
	print("The Square Value of", x, "=", square)  
	
# Create Fuction to get int number	
def get_number():
	while True:
		try:
			# input number
			inputNumber = int(input("Enter Your Number: " )) 
	
		except ValueError:
			print("Only Integer Value Allowed")
	
		else:
			break
	return inputNumber

main()