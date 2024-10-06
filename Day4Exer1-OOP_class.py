class Person:
    # attributes/class members
    name = str()
    age = int()

    # self is a reference to the object/class member/attribute
    def set_details(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is {self.name} an adult? ", end="") # end="" is used to prevent the cursor from moving to the next line

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
if p1.is_adult():
    print("Yes")
else:
    print("No")