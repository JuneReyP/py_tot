# Single Inheritance
class Animal:
    def eat(self):
        print("eating...")
class Dog(Animal):
    def bark(self):
        print("barking...")
puppy = Dog()
puppy.eat()
puppy.bark()