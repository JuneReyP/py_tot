# data encapsulation sample, use __ to make the variable private
class Computer:
    def __init__(self):
        self.__maxprice = 900

    # getter function used to get the price
    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    # setter function used to set the price
    def setMaxPrice(self, price):
        self.__maxprice = price

comp = Computer()
comp.sell()
print("==============")
# change the price directly
comp.__maxprice = 1000
comp.sell()

# using setter function
comp.setMaxPrice(1000)
comp.sell()
#
# class Computer:
#     computername = "Acer Nitro"
#     def __init__(self):
#         self.__price = 62000
#
#     # getter function
#     def sell(self):
#         return self.__price
#
#     # setter function
#     def changePrice(self, newprice):
#         self.__price = newprice
#
# comp = Computer()
# comp.changePrice(15000)
# print(comp.sell())