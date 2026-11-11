import math

<<<<<<< HEAD
def square_root(a):
    # try:
    #     b = math.sqrt(a)
    #     return math.sqrt(b)
    # except:
    #     raise ValueError("Cannot take Square Root of a Negative Number")
    if a < 0:
        raise ValueError("Numbers must be positive for computing hypotenuse")
    return math.sqrt(a)

def hypotenuse(a,b):
    # try:
    #     c = math.hypot(a,b)
    #     if a < 0 or b < 0:
    #         raise ValueError("Numbers must be positive for computing hypotenuse")
    #     return c
    # except ValueError error:
    #     return error
    if a < 0 or b < 0:
        raise ValueError("Numbers must be positive for computing hypotenuse")
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a,b):
    if (a <= 0 or a == 1) or b <= 0:
        raise ValueError("Value Error with Log")
    return math.log(b, a)

def exp(a, b):
    return a ** b

>>>>>>> refs/remotes/origin/main

