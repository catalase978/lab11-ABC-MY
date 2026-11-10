"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        b = math.sqrt(a)
        return math.sqrt(b)
    except:
        raise ValueError("Cannot take Square Root of a Negative Number")

def hypotenuse(a,b):
    try:
        c = math.hypot(a,b)
        if a < 0 or b < 0:
            raise ValueError("Numbers must be positive for computing hypotenuse")
        return c
    except:
        pass

# First example
def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Error, cannot divide by zero")
    return b / a

def logarithm(a,b):
    if (a <= 0 or a == 1) or b <= 0:
        raise ValueError("Value Error with Log")
    return math.log(b, a)

def exponent(a,b):
    return a ** b

