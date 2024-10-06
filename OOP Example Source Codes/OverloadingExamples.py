#Overloading - parameters
def fly(speed, projection):
   print("Dive and Sprint")

def fly(speed):
   print("Dive")

def fly():
   print("Parrot CAN fly")

fly(2)
############################################
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c
# Usage
math = Math()
print(math.add(1))
print(math.add(1, 2))
print(math.add(1, 2, 3))
############################################
class Math:
    def add(self, *args):
        return sum(args)
# Usage
math = Math()
print(math.add(1))
print(math.add(1, 2))
print(math.add(1, 2, 3))
############################################

