def summation(n):
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s

number = int(input("Enter a number: "))
print(f"The summation of {number} is {summation(number)}")