def calculator():
    print("Operators: +, -, *, /, %, ** (power)")

    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif op == "%":
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        result = "Error: Invalid operator"

    print("Result:", result)

calculator()
