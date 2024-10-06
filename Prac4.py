ch = ""
while ch.lower() != "x":
    print("Simple Calculator")
    print("Addition [A]")
    print("Subtraction [S]")
    print("Multiplication [M]")
    print("Division [D]")
    print("Exit [X]")
    ch = str(input("Enter Choices: "))
    if ch.lower() == 'a':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Sum of first and second number: {num1+num2}")
    elif ch.lower() == 's':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Difference of first and second number: {num1 - num2}")
    elif ch.lower() == 'm':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Product of first and second number: {num1 * num2}")
    elif ch.lower() == 'd':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Quotient of first and second number: {num1 / num2}")
    elif ch.lower() == 'x':
        break
    else:
        print("Selected option not available! Please try again.")
    input("Press enter to continue...")