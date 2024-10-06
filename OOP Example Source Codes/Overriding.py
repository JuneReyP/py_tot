class Animal:
    _legs = 4
    def sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    _legs = 2
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())