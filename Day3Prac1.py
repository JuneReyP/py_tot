try:
    ch = ""
    while ch.lower != "x":
        print("Simple Calculator with Exception Handling")
        print("[A] Add")
        print("[S] Subtract")
        print("[M] Multiply")
        print("[D] Divide")
        print("[X] Exit")
        ch = input("Enter choice: ")
        if ch.lower() == "x":
            break
        elif ch.lower() == "a":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Sum is: ", num1 + num2)
        elif ch.lower() == "s":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Difference is: ", num1 - num2)
        elif ch.lower() == "m":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Product is: ", num1 * num2)
        elif ch.lower() == "d":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Quotient is: ", num1 / num2)
        else:
            input("Invalid input. Press any key to continue...")
        check = input("Do you want to continue? [Y/N]: ")
        if check.lower() == "n":
            break
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("Thank you!")