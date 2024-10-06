# class Animal:
#     def eat(self):
#         print("Animal can eat...")
# class Dog(Animal):
#     def eat(self):
#         print("Dog can eat...")
#         super().eat()
#
# par = Dog()
# par.eat()

class Parrot:
    def fly(self):
        print("Parrot can fly...")

    def swim(self):
        print("Parrot can't swim...")

    # def fly(self,speed):
    #
    #     print("Sprint")
    # def fly(self,speed, projection):
    #     print("Dive and sprint")

class Penguin:
    def swim(self):
        print("Penguin can swim...")

    def fly(self):
        print("Penguin can't fly...")
    # def fly(self,speed):
    #     print("Water Sprint")
    #
    # def fly(self,speed, projection):
    #     print("Sprint and Water Dive")

# Create an interface
def test_fly(bird):
    bird.fly(20)

def test_swim(bird):
    bird.swim()

# Create objects
pen = Penguin()
par = Parrot()
# test cases
test_fly(pen)
test_fly(par)
