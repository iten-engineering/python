
from calculator import add, sub, mul, div

while(True):
    try:
        value = input("Calculate : ")
        x, op, y = value.split()
        break
    except:
        print("Ungültige Eingabe: ", value)

map = {'+':add, '&':add, '-':sub, '*':mul, '/':div}
f = map.get(op)

if f is None:
    print("Unknown operator")
elif op == '/' and y == '0':
    print("Division by zero is not allowed")
else:
    res = f(float(x),float(y))
    print(res)