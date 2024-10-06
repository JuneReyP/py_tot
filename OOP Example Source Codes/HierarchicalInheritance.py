class Bird():
    def eat(self):
        print("can eat...")
class Parrot(Bird):
    def fly(self):
        print("can fly...")
class Penguin(Bird):
    def swim(self):
        print("can swim...")
par = Parrot()
print(par.fly())
print(par.eat())
pen = Penguin()
print(pen.swim())
print(pen.eat())


