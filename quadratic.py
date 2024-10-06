import math
class Quadratic:
    def __init__(self):
        self.a = self.getA()
        self.b = self.getB()
        self.c = self.getC()
        print("")

    def getA(self):
        self.a = int(input("Enter coefficient a: "))
        return self.a

    def getB(self):
        self.b = int(input("Enter coefficient b: "))
        return self.b

    def getC(self):
        self.c = int(input("Enter coefficient c: "))
        return self.c

    def evaluate(self, x):
        return self.a * x * x + self.b * x + self.c

    def dicrimant(self):
        return int(self.b**2 - 4 * self.a * self.c)

    def isImaginaryRoots(self):
        return self.dicrimant() < 0

    def isRealRoots(self):
        return self.dicrimant() >= 0

    # these methods can only be invoked if the roots are not imaginary
    def firstRoots(self):
        x1 = float((-self.b + math.sqrt(self.dicrimant())) / (2 * self.a))
        return x1

    def secondRoots(self):
        x2 = float((-self.b - math.sqrt(self.dicrimant())) / (2 * self.a))
        return x2

    def isPerfectSquare(self):
        if self.firstRoots() == self.secondRoots():
            return "It is a perfect square."
        else:
            return "It is not a perfect square."

    def display(self):
        print(f"Quadratic expression is: {self.a}x^2 + {self.b}x + {self.c}")
        if self.isImaginaryRoots():
            print("The roots are imaginary.", end="\n\n")
        else:
            print(f"The roots are real: x1 = {self.firstRoots()}; x2 = {self.secondRoots()}")
            print(self.isPerfectSquare(), end="\n\n")

        print("Evaluating the expression:")
        x = int(input("Enter x: "))
        print(f"Result: {self.evaluate(x)}")


sample = Quadratic()
sample.display()
