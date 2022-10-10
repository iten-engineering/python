
def max(x, y, z=None):
    if z == None:
        return x if x > y else y
    if x > y and x > z:
        return x
    elif y > z:
        return y
    return z


print("max(1,2) =", max(1,2))
print("max(2,1) =", max(2,1))
print("max(9,-15,-12) =", max(9,-15,-12))
print("max(9, 15,-12) =", max(9, 15,-12))
print("max(9,-15, 12) =", max(9,-15, 12))
