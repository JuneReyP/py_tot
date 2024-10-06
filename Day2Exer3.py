# Local variable
# def sum():
#     s = 1+3
#     print(s)
#
# sum()

# Global variable
global x
x = 10
def sum():
    # s = x
    global s
    s = 1
    return s

print(sum())
print(s)

