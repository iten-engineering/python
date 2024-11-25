
f = lambda x: 0.5 * x  + 1

print(f(0))
print(f(2))

x_values = [-3,-2,-1,0,1,2,3]

for x in x_values:
    print(f"x={x}: y={f(x)}")