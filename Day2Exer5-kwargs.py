# keyword arguments(**kwargs)
def myfunction(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

myfunction(name="John", age = 30, city = "New York")