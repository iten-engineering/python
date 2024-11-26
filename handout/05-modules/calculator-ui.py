from calculator import add, sub, mul, div

map = {"+": add, "-":sub, "*":mul, "/":div, "&":add}

value = input("Calculate: ")
x, op, y = value.split()

f = map.get(op)

if f is None:
    print(f"Unbekannter operator {op}")
elif op == "/" and y == "0":
    print("Division durch 0 ist nicht erlaubt")
else:
    print(f(float(x),float(y)))