print("Welcome to the Simple Calculator!")

a = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
b = float(input("Enter the second number: "))

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = a / b
else:
    result = "Invalid operation"

print("Result:", result)
