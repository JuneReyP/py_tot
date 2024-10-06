# Multilevel
class Animal:
    def eat(self):
        print("eating...")
class Dog(Animal):
    def bark(self):
        print("barking...")
class BabyDog(Dog):
    def weep(self):
        print("weeping...")

preppy = BabyDog()
preppy.weep()
preppy.bark()
preppy.eat()

