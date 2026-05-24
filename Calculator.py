def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def div(a, b):
    return a/b
def mult(a, b):
    return a*b
print('Enter operation you want to do, a. Add, b. Subtract c. Multiply d. Division')
operation = input()
print("Enter first number")
a = int(input())
print("Enter second number")
b = int(input())
if (operation == "a"):
    print("Result: " + str(add(a, b)))
if (operation == "b"):
    print("Result: " + str(sub(a, b)))
if (operation == "c"):
    print("Result: " + str(mult(a, b)))
if (operation == "d"):
    print("Result: " + str(div(a, b)))