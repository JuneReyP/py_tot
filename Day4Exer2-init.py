class Person:
    # attributes/class members
    name = str()
    age = int()

    # constructor is a special method that is called when an object is created, it is used to initialize the object
    def __init__(self):
        print("Executing...")

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