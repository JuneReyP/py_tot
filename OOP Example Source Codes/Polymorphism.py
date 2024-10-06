#Overloading - parameters
# Ability to define multiple methods with the same name but different parameters
class Parrot:
    def fly(self):
        print("Parrot CAN fly")
    def swim(self):
        print("Parrot CAN'T swim")
class Penguin:
    def swim(self):
        print("Penguin CAN swim")
    def fly(self):
        print("Penguin CAN'T fly")

def test_fly(bird):
    bird.fly()
def test_swim(bird):
    bird.swim()

pen = Penguin()
par = Parrot()
#Test Case
test_fly(pen)
test_fly(par)



