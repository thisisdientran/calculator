# Program make a simple calculator that can add, subtract, multiply and divide using functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

choice = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
else:
    print(divide(num1, num2))