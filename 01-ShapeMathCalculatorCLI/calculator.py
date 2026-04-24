# Mini-project #1: Simple Calculator

history = []

while True:
    print("""
    --- Simple Calculator ---
    1. Perform calculation
    2. Show history
    3. Clear history
    4. Quit program
    """)



    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    op = input("Enter operation (+, -, *, /, //, %, **): ")
    match op:
        case "+":
            print(f"{num1} + {num2} = {num1 + num2}")
            history.append(num1 + num2)
        case "-":
            print(f"{num1} - {num2} = {num1 - num2}")
            history.append(num1 + num2)
        case "*":
            print(f"{num1} * {num2} = {num1 * num2}")
            history.append(num1 + num2)
        case "/":
            try:
                print(f"{num1} / {num2} = {num1 / num2}")
                history.append(num1 + num2)
            except ZeroDivisionError:
                print("Division by zero is not possible.")
                continue
        case "//":
            print(f"{num1} // {num2} = {num1 // num2}")
            history.append(num1 + num2)
        case "%":
            print(f"{num1} % {num2} = {num1 % num2}")
            history.append(num1 + num2)
        case "**":
            print(f"{num1} ** {num2} = {num1 ** num2}")
            history.append(num1 + num2)

    answer = input("Do you want to exit? (y/n): ")
    if answer.lower().strip() == "y":
        print("Program ended!")
        break
