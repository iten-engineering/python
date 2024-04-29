names = ["Peter", "Jane", "Fred"]
ages = [31, 35, 4]
vip = [True, False, False]

for t in zip(names, ages, vip):              # use a tuple
    print(t)

for name, age in zip(names, ages):
    if age >= 18:
        print(name, "ist >= 18")
    else:
        print(name, "ist < 18")

l = len(ages)
print(l)
print(list(range(l)))