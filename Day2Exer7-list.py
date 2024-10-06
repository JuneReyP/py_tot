# python list - changeable data, uses square brackets
fruit = ["apple","orange","kiwi","zuchini"]
fruit.append("banana")
fruit.insert(1,"jackfruit")
x = 1
for f in fruit:
    print(f"{x}. {f}")
    x+=1

print(fruit[2])
fruit.remove("apple")

print(list("ford"))