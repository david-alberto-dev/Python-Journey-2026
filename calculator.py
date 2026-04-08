"""
Miniproject #1: Simple Calculator
"""

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    op = input("Enter operation (+, -, *, /, **): ")

    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        try:
            print(f"{num1} / {num2} = {num1 / num2}")
        except ZeroDivisionError:
            print("Division by zero is not possible.")
            continue
    elif op == "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    else:
        print("Please enter a valid operation! Only +, -, *, /, **")
        continue

    answer = input("Do you want to exit? (y/n): ")
    if answer.lower().strip() == "y":
        print("Program ended!")
        break