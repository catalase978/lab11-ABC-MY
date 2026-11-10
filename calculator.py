import math

<<<<<<< HEAD
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithmic base or argument.")
    return math.log(b, a)

def exp(a, b):
=======

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def logarithm(a,b):
    if (a <= 0 or a == 1) or b <= 0:
        raise ValueError("Value Error with Log")
    return math.log(b, a)

def exponent(a,b):
    return a ** b

