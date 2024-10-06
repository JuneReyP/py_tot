from tkinter import *  # Import tkinter library (*) as wildcard

expr = ""  # global variable


def clear():
    result.set("")
    global expr
    expr = ""


def process(value):
    global expr
    expr = expr + str(value)
    result.set(expr)


def evaluate():
    global expr
    r = eval(expr)  #  eval() function evaluates the “String” like a python expression and returns the result as an integer. Uses PMDAS rule
    result.set(str(r))
    expr = ""


window = Tk()  # Create a window
window.geometry("400x300")  # Set the window size
window.resizable(0, 0)  # Set the window to non-resizable
window.title("Simple Calculator")  # Set the window title
window.configure(bg="light blue")  # Set the window background color

# String variable declaration to store the result
result = StringVar()  # Create a string variable

resE = Entry(window, bd=3, font="Tahoma", textvariable=result, justify=RIGHT, state=DISABLED)  # Create an entry widget, textvariable is set to result and will be used to display the result
resE.place(x=50, y=30, width=310, height=40)  # Place the entry widget on the window

seven = Button(window, text="7", font="Tahoma", width=7, command=lambda: process(7))  # Create a button widget with text 7, lambda function is used to pass the value to the process function
seven.place(x=50, y=80)  # Place the button on the window

eight = Button(window, text="8", font="Tahoma", width=7, command=lambda: process(8))
eight.place(x=125, y=80)

nine = Button(window, text="9", font="Tahoma", width=7, command=lambda: process(9))
nine.place(x=200, y=80)

div = Button(window, text="/", font="Tahoma", width=7, command=lambda: process("/"))
div.place(x=275, y=80)

four = Button(window, text="4", font="Tahoma", width=7, command=lambda: process(4))
four.place(x=50, y=120)

five = Button(window, text="5", font="Tahoma", width=7, command=lambda: process(5))
five.place(x=125, y=120)

six = Button(window, text="6", font="Tahoma", width=7, command=lambda: process(6))
six.place(x=200, y=120)

mul = Button(window, text="*", font="Tahoma", width=7, command=lambda: process("*"))
mul.place(x=275, y=120)

one = Button(window, text="1", font="Tahoma", width=7, command=lambda: process(1))
one.place(x=50, y=160)

two = Button(window, text="2", font="Tahoma", width=7, command=lambda: process(2))
two.place(x=125, y=160)

three = Button(window, text="3", font="Tahoma", width=7, command=lambda: process(3))
three.place(x=200, y=160)

sub = Button(window, text="-", font="Tahoma", width=7, command=lambda: process("-"))
sub.place(x=275, y=160)

zero = Button(window, text="0", font="Tahoma", width=7, command=lambda: process(0))
zero.place(x=50, y=200)

equal = Button(window, text="=", font="Tahoma", width=7, command=evaluate)
equal.place(x=125, y=200)

clear = Button(window, text="Clear", font="Tahoma", width=7, command=clear, bg="aqua", fg="red")  #fg is for text color and bg is for background color
clear.place(x=200, y=200)

add = Button(window, text="+", font="Tahoma", width=7, command=lambda: process("+"))
add.place(x=275, y=200)

window.mainloop()  # Start the main loop of the window
