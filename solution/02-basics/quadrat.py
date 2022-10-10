
num = 1
square = num**num                           # Square with the '**' operator

while square <= 15:
    print(num, "x", num, "=", square)
    num = num + 1
    square = pow(num, 2)                    # Square with the pow function
