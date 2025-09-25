def perform_operation(num1,num2,operation):
	
	match operation:
		case "add":
			result = num1 + num2

		case "subtract":
			result = num1 - num2

		case "multiply":
			result = num1 * num2

		case "divide":
			if num2 == 0:
				print("You cannot divide by zero")
				result = "Error"
			else:
				result = num1 / num2
		case _:
			print("Invalid operation")
			result = "Error"


	return result
	

