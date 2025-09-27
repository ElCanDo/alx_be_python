FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def  convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to convert: "))
convert = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if convert == "F":
    result = convert_to_celsius(temp)
    print(f"{temp}°{convert} is {result:.2f}\u00B0C")
elif convert == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}\u00B0{convert} is {result:.2f}\u00B0F")
else:
    print("Error")

