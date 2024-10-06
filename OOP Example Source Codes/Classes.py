class Person:
    name = str()
    age = int()
    def set_details(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is {self.name} an adult?: ",end="")
    def is_adult(self):
        return self.age >= 18

p1 = Person()
p2 = Person()

p1.set_details("Juan", 25)
p2.set_details("Pedro", 17)

p1.display()
if p1.is_adult():
    print("Yes")
else:
    print("No")

p2.display()
if p2.is_adult():
    print("Yes")
else:
    print("No")



