from calculator import Calculator as calc


data = input("Calculate: ")
x, op, y = data.split()

map = {"+": calc.add, "-": calc.sub, 
       "*": calc.mul, "/": calc.div,
       "&": calc.add }

f = map.get(op)

if f == None:
    print("Ungültiger operator:", op)
elif op == "/" and y == "0":
    print("Division durch 0 ist nicht erlaubt")
else:
    result = f(float(x),float(y))
    print(result)




