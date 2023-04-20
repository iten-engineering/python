
square = lambda x : x * x

print(square(4))
print(square(-2))
print(square(3))


print("apply sample:")

def apply(numbers, func):
    result_list = []
    for n in numbers:
        result = func(n)
        result_list.append(result)
    return result_list


values = [5, -12, 6.4, -3, 9.9]

results= apply(values, square)
print(results)

results= apply(values, abs)
print(results)

results= apply(values, lambda x : 2*x)
print(results)

