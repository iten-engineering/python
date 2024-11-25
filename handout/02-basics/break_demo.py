
find = 99
numbers = [7, 12, 99, 55, 100, 233]



for pos, number in enumerate(numbers):
    print(pos, number)
    if find == number:
        print(pos)
        break
