
numbers = list(range(1,21))
print(numbers)

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

odd_numbers = list(filter(lambda n: n % 2 == 1, numbers))

print(even_numbers)
print(odd_numbers)
