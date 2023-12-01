
numbers = [1,4,-5,7,-9]

res = list(map(abs, numbers))
print(numbers)
print(res)

def double(x):
    return 2 * x

res = list(map(double, numbers))
print(numbers)
print(res)


res = list(map(lambda x: x * 3, numbers))
print(numbers)
print(res)

