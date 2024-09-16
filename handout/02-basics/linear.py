
def f_linear(x):
    y = 0.5 * x + 1
    return y

f = lambda x : 0.5 * x + 1

x_list = [-3,-2,-1,0,1,2,3]

for x in x_list:
    y = f(x)
    print(x, ":", y)
