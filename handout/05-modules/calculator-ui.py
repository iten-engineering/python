# import calculator
# calculator.add(1,2)

from calculator import add, sub, mul, div

data = input("Calculate = ")
x, op, y = data.split()

op_map = {
    "+":add, 
    "-":sub, 
    "*":mul, 
    "/":div, 
    "&":add,
    "add": add}


# f = op_map[op]    # wirft Exception falls key nicht vorhanden in map
f = op_map.get(op)  # gibt None zurück, falls key nicht existiert

if f is None:
    print(f"Unkown operator: {op}")
elif op == "/" and y == "0":
    print("Division by zero")
else:
    res = f(float(x),float(y))
    print(res)