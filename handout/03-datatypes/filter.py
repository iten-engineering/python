
numbers = list(range(1,21))
print(numbers)

even_numbers = list( filter(lambda n: n %2 == 0, numbers) )
print(even_numbers)

odd_numbers = list( filter(lambda n: n %2 == 1, numbers) )
print(odd_numbers)