class Animal:
    def speak(self):
        return "Animal speaks"
class Bird(Animal):
    def fly(self):
        return "Bird can fly"
class Fish(Animal):
    def swim(self):
        return "Fish can swim"
class Penguin(Bird, Fish):
    def walk(self):
        return "Penguin can walk"
# Create an instance of Penguin
penguin = Penguin()
# Access methods from parent classes
print(penguin.speak())  # Inherited from Animal
print(penguin.fly())    # Inherited from Bird
print(penguin.swim())   # Inherited from Fish
print(penguin.walk())   # Defined in Penguin
