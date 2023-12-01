def max(x, y, z=None):
    if isinstance(z, type(None)):
        return x if x > y else y
    if x > y and x > z:
        return x
    elif y > z:
        return y
    return z


print(max(1,4))

def get_person():
    return "Anna", 12, "Bern"

result = get_person()
print(result)

x, y = [12, 24]
print(x, y)

