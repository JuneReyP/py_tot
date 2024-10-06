from MyPackage import MathOperations as m

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
print("===========================")
print(f"Sum of {n1} and {n2} is {m.add(n1, n2)}")
print(f"Difference of {n1} and {n2} is {m.subtract(n1, n2)}")
print(f"Product of {n1} and {n2} is {m.multiply(n1, n2)}")
print(f"Qoutient of {n1} and {n2} is {m.divide(n1, n2)}")