# 1. Construct a code snippet that assigns `True` to the variable `result` if the variable `x` is
# less than `y` and `y` is less than `z`, or if the sum of `x` and `z` is not greater than twice
# the value of `y`. Use the values `x = 5`, `y = 10`, and `z = 15`.
# answer:
# result = bool()
# x, y, z = 5, 10, 15
# if (x < y and y < z) or ((x + z) < y * 2):
#     result = True
#     print(result)


# 2. Write a code snippet that assigns a grade based on the variable `score`. If `score` is 90
# or above, assign 'A'; if `score` is 80 or above but less than 90, assign 'B'; if `score` is 70 or
# above but less than 80, assign 'C'; otherwise, assign 'F'. Use the value `score = 85`
# answer:
# score = 85
# if score >= 90:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# else:
#     print("Grade: F")

# 3. Write a code snippet to calculate the product of all numbers in the list `numbers = [2, 3,
# 5, 7, 11]` using a `for` loop and store the result in a variable named `product`.
# answer:
# numbers = [2, 3, 5, 7, 11]
# product = 0
# for i in numbers:
#     product += i
# print(product)

# 4. Write a code snippet that iterates over the numbers from 0 to 9. Skip even numbers and
# stop the loop if the number 7 is encountered. Print each remaining number
# answer: ===============================================================================================
# i = 0
# while i != 9:
#     if i % 2 == 0:
#         # print("1st")
#         continue
#     elif i == 7:
#         print(i)
#         break
#     i += 1
# print(i)

# 5. Define a function named `add` that takes two parameters and returns their sum. Use the
# function to add the numbers 3 and 4, and print the result
# answer:
# def add(num1, num2):
#     print(num1 + num2)
# add(3,4)

# 6. Define a function named `func` that takes two parameters: `x` and `y` with a default
# value of 10. The function should return the sum of `x` and `y`. Call the function twice: first
# with the value 5, and then with the values 5 and 15. Print the results of both calls
# answer:
# def func(x=10, y=10):
#     return x + y
# print(func(5))
# print(func(5, 15))

# 7. Define a function named `is_even` that takes a number as a parameter and returns
# `True` if the number is even, otherwise `False`. Print the result on the screen as “Even” or
# “Odd”.
# answer:
# def is_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(is_even(1))

# 8. Define a variable `x` with the value 10. Define a function named `change` that uses the
# `global` keyword to modify the value of `x` to 20. Call the function `change` and print the
# value of `x`
# answer:
# x = 10
# def change():
#     global x
#     x = 20
#     print(x)
# change()

# 9. Define a function named `func` that accepts any number of positional and keyword
# arguments. The function should return a tuple containing the positional arguments and a
# dictionary of the keyword arguments. Call the function with the arguments `1, 2, 3, a=4,
# b=5` and print the result.
# answer: ===========================wala ko ka downlaod pdf copy sir ang *args=======================================
# def func():


# 10. Define a recursive function named `factorial` that calculates the factorial of a given
# number `n`. Use this function to calculate the factorial of 5 and print the result
# answer:
# def factorial(n):
#     i = 1
#     s = 1
#     while i <= n:
#         s *= i
#         i += 1
#     return s
#
# print(factorial(5))


# 11. Given a list `list = [1, 2, 3, 4, 5]`, write a code snippet to replace the third and fourth
# elements with the values 8 and 9. Print the modified list
# answer:
# list = [1, 2, 3, 4, 5]
# list[2] = 8
# list[3] = 9
# print(list)

# 12. Given a tuple `t = (1, 2, 3)`, write a code snippet to try to change the second element
# to 4 and catch the `TypeError` that is raised. Print the error message
# answer:
# try:
#     t = (1, 2, 3)
#     t[1] = 4
# except:
#     print("Snytax Error")

# 13. Given a set `s = {1, 2, 3, 4, 5}`, write a code snippet to add the value 6 and remove
# the value 1 from the set. Print the modified set using for loop
# answer:
# s = {1, 2, 3, 4, 5}
# s.add(6)
# print(s)
# s.remove(1)
# print(s)


# 14. Given a dictionary `d = {'a': 1, 'b': 2, 'c': 3}`, write a code snippet to add a new keyvalue pair `'d': 4` and delete the key `'b'`. Print the modified dictionary using for loop.
# answer:
# d = {'a': 1, 'b': 2, 'c': 3}
# # wala ko ka download PDF file sa diri nga topic sir
# d.pop("b")
# print(d)

# 15. Write a code snippet to import the `math` module and print the square root of 16
# using the `sqrt` function from the module
# answer:
# import math
# print(math.sqrt(16))

# 16. Write a code snippet to import the `random` module and print a random integer
# between 1 and 10 (inclusive) using the `randint` function
# answer:
# import random
# print(random.randint(1,10))

# 17. Write a code snippet that tries to divide 10 by 0 and catches the `ZeroDivisionError`
# exception. Assign the string 'undefined' to the result if the exception is caught. Print the
# result
# answer:
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Number can't be devided to zero")


# 18. Write a code snippet that tries to access the sixth element of the list `lst = [1, 2, 3]`
# and catches the `IndexError` exception. Print the exception message
# answer:
# try:
#     lst = [1, 2, 3]
#     lst[5]
# except IndexError:
#     print("Can't access index")


# 19. Define a class named `MyClass` with an `__init__` method that takes a parameter
# `value` and assigns it to an instance variable. The class should also have a method named
# `display` that prints the instance variable. Create an instance of the class with the value 10
# and call the `display` method
# answer:
# class MyClass:
#     def __init__(self, value):
#         self.var = value
#
#     def display(self):
#         print(self.var)
#
# sample = MyClass(10)
# sample.display()



# 20. Define a class named `Person` with a class variable `species` set to "Homo sapiens".
# The class should also have an `__init__` method that takes a parameter `name` and
# assigns it to an instance variable. Create two instances of the class with the names "Alice"
# and "Bob" and print whether their `species` attributes are equal. Print whether species attributes are equal
# answer:
# class Person:
#     __species = "Homo sapiens"
#     def __init__(self, name):
#         print(self.__species)
#
# Alice = Person("Alice")
# bob = Person("Bob")