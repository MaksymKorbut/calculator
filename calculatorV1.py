import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
    
def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error! Square root of a negative number."

# Пример использования
print("Addition:", add(2, 3))
print("Subtraction:", subtract(5, 2))
print("Multiplication:", multiply(3, 4))
print("Division:", divide(10, 2))