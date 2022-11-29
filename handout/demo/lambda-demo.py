
def add2(a,b):
    return a + b

add=lambda a, b :  a \
    + b

print(add(1,4))
print( add2(1,4) )

numbers = [1,3,4,5,9]
n = "Hello"

def apply(n_list, func):
    results = []
    for n in n_list:
        result = func(n)
        results.append(result)
    return results

results = apply(numbers, lambda x: x*2)
print(results)

