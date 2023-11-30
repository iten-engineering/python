
def linear(x):
    y = 0.5 * x + 1
    return y

linear2 = lambda x : 0.5 * x + 1

for x in range(-3, 4):   
    y = linear2(x)
    print(x, ":", y)
