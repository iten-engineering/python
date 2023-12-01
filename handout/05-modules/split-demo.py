from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

def split(data, op):
    idx = data.index(op)
    x = data[:idx].strip()
    y = data[idx+1:].strip()
    op= data[idx:idx+1]
    return float(x), op, float(y)

def split_all(data, operators):
    for op in operators:
        if op in data:
            return split(data, op)
    raise Exception("Unsupported Operator")

map = {"+" : add, "-" : sub, "*" : mul, "/" : div, "&": add, "_": sub}

tests = ["1 / 0", "1+1", "  1 * 5", "  1 & 4", "6_2"]

for data in tests:
    print("--------------")
    print(data)    
    try:
        x, op, y = split_all(data, map.keys())
        f = map.get(op)
        result = f(x, y)
        print(result)
    except Exception as e:
        print(str(e))
