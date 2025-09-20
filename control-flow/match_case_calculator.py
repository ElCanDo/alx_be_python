
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+,-,*,/): ")

match operation:

    case "+":
        result = num1 + num2

    case "-":
        result = num1 - num2

    case "*":
        result = num1 * num2

    case "/":
        if num2 == 0:
            print("You cannot divide by zero.")
            result = "Error"
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")
        result = "Error."

print(f"The result is {result}.")
