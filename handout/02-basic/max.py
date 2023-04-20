
def max(x, y, z=None):
    if z == None:
        return x if x > y else y
    if x > y and x > z:
        return x
    return y if y > z else z

print(max(1,2))
print(max(2,1))

print(max(1,2,3))
print(max(2,3,1))
print(max(3,2,1))
