from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

data = input("Calculate: ")
tokens = data.split()

x, op, y  = tokens

map = {"+" : add, "-" : sub, "*" : mul, "/" : div }
f = map.get(op)

if f == None:
    print("Unknown operator")
elif (f == div and y == "0"):
    print("Division by zero")
else:
    print( f(float(x),float(y)) )


