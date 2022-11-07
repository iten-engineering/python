
f1 = lambda x: 0.5 * x  + 1

def f2(x):
    y = 0.5 * x  + 1
    return y

x_values = [-3,-2,-1,0,1,2,3] 
for x in range(-3,4):           # range anstelle von x_values
    y = f2(x)
    print("x=", x, "y=",y)

