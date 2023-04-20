
numbers = [1,2,3,4,5]

# break 
print("break:")
for n in numbers:
    if n > 3:
        break
    print(n)


# continue
print("continue:")
for n in numbers:
    if (n % 2) == 1:
        continue
    print(n)
