class Robot:
    __hp = 10 # private variable ,can be accessed only within the class robot
    _speed = 5 # protected variable, can be accessed within the class and its child class

    def walk(self):
        print("can walk...")

    #getter method, used to access the private variable
    def gethp(self):
        return self.__hp

#single inheritance, gizmo is a child class of robot
class Gizmo(Robot):
    def swim(self):
        print("can swim...")
        print(self._speed)
    def getspeed(self):
        return self._speed

g = Gizmo()
g.swim()

r = Robot()
print(f"{r.gethp()}")