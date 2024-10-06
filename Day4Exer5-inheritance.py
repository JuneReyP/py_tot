#single inheritance
# Parent class
# class Animal:
#     def eat(self):
#         print("eating...")
#
# class Dog(Animal): # Dog is a child class of Animal
#     def bark(self):
#         print("barking...")
#
# puppy = Dog()
# puppy.eat()
# puppy.bark()


# multi level inheritance
# class Animal:
#     def eat(self):
#         print("eating...")
#
# class Dog(Animal): # Dog is a child class of Animal
#     def bark(self):
#         print("barking...")
#
# class BabyDog(Dog): # BabyDog is a child class of Dog
#     def weep(self):
#         print("weeping...")
#
# print("===============")
# baby = BabyDog()
# baby.eat()
# baby.bark()
# baby.weep()

# Hierarchical inheritance
# class Bird():
#     def eat(self):
#         print("can eat...")
# class Parrot(Bird):
#     def fly(self):
#         print("can fly...")
# class Penguin(Bird):
#     def swim(self):
#         print("can swim...")
#
# par = Parrot()
# print(par.fly())
# print(par.eat())
# print("===============")
# pen = Penguin()
# print(pen.swim())
# print(pen.eat())

# multiple inheritance
# class Animal:
#     def speak(self):
#         return "Animal Speaks"
# class Bird(Animal):
#     def fly(self):
#         return "Bird can fly..."
# class fish(Animal):
#     def swim(self):
#         return "Fish can swim..."
# class Penguin(Bird, fish):
#     def walk(self):
#         return "Penguin can walk..."
#
# penguin = Penguin()
# #access methods from the parent classes
# print(penguin.speak()) # Inherited from Animal class
# print(penguin.fly()) # Inherited from Bird class
# print(penguin.swim()) # Inherited from fish class
# print(penguin.walk()) # Inherited from Penguin class
