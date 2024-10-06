import math
class Computer:
    computername = "Acer Nitro"
    def __init__(self):
        self.__price = 62000
    def sell(self): # getter method
        #return self.__price
        print(f"The computer name is {self.computername}")
        print(f"The selling price is {self.__price}")
    def changePrice(self, newprice): #setter method
        self.__price = newprice
comp = Computer() # creation of an object
comp.changePrice(15000)
comp.sell()
