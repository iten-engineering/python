
numbers = [12,-6, 9, 15, -3]
print(numbers)

abs_numbers = []
for n in numbers:
    res = abs(n)
    abs_numbers.append(res)
print(abs_numbers)


double_numbers = []
for n in numbers:
    res = n * 2
    double_numbers.append(res)
print(double_numbers)


def apply(numbers, f):
    results = []
    for n in numbers:
        res = f(n)
        results.append(res)
    return results

abs_numbers2 = apply(numbers, abs)
print(abs_numbers2)

def double(x):
    return 2 * x

double_numbers2 = apply(numbers, double)
print(double_numbers2)

triple_numbers = apply(numbers, lambda x: 3*x)
print(triple_numbers)