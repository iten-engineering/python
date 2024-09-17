from calc import add, sub, mul, div

value = input("Calculate: ")

x, op, y = value.split()
x_num = float(x)
y_num = float(y)

map = {"+":add, "-":sub, "*":mul, "/":div, "&":add}
f = map.get(op)

if f is None:
    print("Unsupported operator!")
elif f == div and y == "0":
    print("Division by zero!")
else:
    print( f(x_num, y_num))


