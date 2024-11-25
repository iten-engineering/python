
numbers = [-5, -2, 0, 5, 9, 77]
print(numbers)

def double_numbers(numbers):
    results = []
    for number in numbers:
        result = 2 * number
        results.append(result)
    return results

numbers2 = double_numbers(numbers)
print(numbers2)


def apply(numbers, func):
    results = []
    for number in numbers:
        result = func(number)
        results.append(result)
    return results

def triple(number):
    return 3 * number

numbers3 = apply(numbers, triple)
print(numbers3)

numbers4 = apply(numbers, lambda number: 4*number)
print(numbers4)

numbersAbs = apply(numbers, abs)
print(numbersAbs)