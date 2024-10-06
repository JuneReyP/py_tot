# upper() - Converts a string into upper case
ms = "I love Python"
output = ms.upper()
print(output)

# lower() - Converts a string into lower case
ms = "I love Python"
output = ms.lower()
print(output)

# capitalize() - Converts the first character to uppercase
ms = "I love Python"
output = ms.capitalize()
print(output)

# title() - Converts the first character of each word to uppercase
ms = "I love Python"
output = ms.title()
print(output)

# split() - Splits the string at the specified separator, and returns a list
ms = "I lov#e Py#tho#n Progr#amming"
output = ms.split("#")
print(output)

# replace() - Returns a string where a specified value is replaced with a specified value
ms = "I love Python"
output = ms.replace("Python", "Java")
print(output)

# len() - count characters in a string
ms = "I love Python"
l = len(ms)
print(l)

# count() – Returns the number of times the value appears in the string
ms = "I love Python. Python is my favorite programming language."
c = ms.count("Python")
print(c)