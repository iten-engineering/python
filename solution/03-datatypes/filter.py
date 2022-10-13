
# create numbers
numbers = list(range(1,21))
print(numbers)

# filter even numbers with loop
even_numbers = []

def even(number):
    return True if (number % 2) == 0 else False

for number in numbers:
    if (even(number)):
        even_numbers.append(number)
print(even_numbers)

# filter odd numbers with filter
def odd(number):
    return False if (number % 2) == 0 else True

odd_numbers = list(filter(odd, numbers))
print(odd_numbers)

