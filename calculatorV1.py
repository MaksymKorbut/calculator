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
    return a ** b

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error! Square root of negative number."

def main():
    print("Simple Calculator")
    print("Enter the operation you want to perform:")
    print("Addition: +")
    print("Subtraction: -")
    print("Multiplication: *")
    print("Division: /")
    print("Power: **")
    print("Square Root: sqrt")

    while True:
        num1 = float(input("Enter first number: "))
        choice = input("Enter operation (+, -, *, /, **, sqrt): ")

        if choice in ['+', '-', '*', '/', '**']:
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '**':
                print(f"{num1} ** {num2} = {power(num1, num2)}")

        elif choice == 'sqrt':
            print(f"sqrt({num1}) = {sqrt(num1)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()