# import calculator
# calculator.add(1,2)

from calculator import add, sub, mul, div

data = input("Calculate = ")
x, op, y = data.split()

map = {"+":add, "-":sub, "*":mul, "/":div, "&":add,
       "add": add}

f = map.get(op)

if f is None:
    print(f"Unkown operator: {op}")
elif op == "/" and y == "0":
    print("Division by zero")
else:
    res = f(float(x),float(y))
    print(res)