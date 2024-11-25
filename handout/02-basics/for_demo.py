
names = ["sam", "lea", "anna"]
ages = [12, 19, 17]
vips = [False, True, False]

for t in zip(names, ages):
    print(t[0], t[1])

for name, age in zip(names, ages):
    print(name, age)    

for age, name, vip in zip(names, ages, vips):
    print(age, name, vip)

for n in range(10,101,10):
    print(n)

for index, name in enumerate(names):
    print(index, name)