#user greeting
print('Hello, User')
print('You can perform one of the following operations: +, -, *, /')

#input first number
num1 = float(input('iput first number: '))

#input operation
operation = input('input operation (+, -, *, /): ')

#input second number
num2 = float(input('input second number: '))

def calculator_basic 
    #performing an operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'ERROR! DIVISION BY ZERO.'
    else:
        result = "ERROR! INCORRECT OPERATION."

#output result
print('Result:', result)
