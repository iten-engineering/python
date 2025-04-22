
names = ["Anna", "Lea", "Sam"]
ages = [15,66,43]
vips = [True, False, True]

for t in zip(names, ages):
    print(t[0], t[1])

for name, age, vip in zip(names, ages, vips):
    print(name, age, vip)    