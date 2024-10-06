class Person:
    # Attributes
    name = ""
    # Constructor
    def __init__(self, n):
        self.name = n
    # Methods
    def changeName(self, n):
        self.name = n
    def displayInfo(self):
        print(f"Name: {self.name}")

chad =  Person("John Doe") # Instance object creation
chad.displayInfo()
