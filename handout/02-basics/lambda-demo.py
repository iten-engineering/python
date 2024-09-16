
def triple(x):
    return 3 * x

numbers = list(range(-5,6))
print(numbers)

def apply(numbers, f):
    result = []
    for n in numbers:
        rn = f(n)
        result.append(rn)
    return result

print( apply(numbers, lambda x : 2 * x))
print( apply(numbers, triple))
print( apply(numbers, abs))


print(triple())



