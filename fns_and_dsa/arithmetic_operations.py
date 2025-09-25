def perform_operation(num1,num2,operation):
	num1 = float()
	num2 = float()
	operation = str("add,subtract,multiply,divide")
	
	if operation == "add":
		result = num1 + num2

	elif operation == "subtract":
		result = num1 - num2

	elif operation == "multiply":
		result = num1 * num2

	elif operation == "divide":
		if num2 == 0:
			print("You cannot divide by zero")
			result = "Error"
		else:
			result = num1 / num2
	else:
		print("Invalid operation")
		result = "Error"


	return result
	

