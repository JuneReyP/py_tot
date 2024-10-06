# Recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n - 1)

# test the function
print(factorial(5))