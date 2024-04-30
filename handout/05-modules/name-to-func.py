import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Variable op holds the name of the function we want to call
op = "add"

# Get the function based on the string value stored in op
operation = getattr(sys.modules[__name__], op)

# Call the function with the desired arguments
result = operation(10, 5)

print(result)  # Output will be 15
