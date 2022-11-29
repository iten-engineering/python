
numbers = list( range(1,21) )
print(numbers)

def even(number):
    return True if (number % 2) == 0 else False

def even2(number):
    if (number % 2) == 0:
        return True
    else: 
        return False

print(even(12))
print(even(15))

even_numbers = list( filter(even, numbers) )
print(type(even_numbers))
print(even_numbers)

odd_numbers = list( filter(lambda n: n % 2 == 1, numbers) )
print(odd_numbers)
