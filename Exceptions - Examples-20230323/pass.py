def main():
    x = get_number("Enter Your Number: ")
    square = x * x
	# printing the square root of a number
    print("The Square Value of", x, "=", square)  
	
# Create Fuction to get int number	
def get_number(message):
	while True:
		try:
			# input number
			return  int(input(message)) 
	
		except ValueError:
			pass
main()