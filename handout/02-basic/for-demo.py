
numbers = list(range(0,10))

for n in numbers:
    even = (n%2) == 0
    if even:
        print(n)


# filter values with continue
fruits = ["Apple", "Banana", "Cherry", "Ananas"]
a_fruits = []

for f in fruits:
    if not f.startswith("A"):
        continue
    print(f)
    a_fruits.append(f)

print(a_fruits)






