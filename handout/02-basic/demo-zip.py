

names = ["Peter", "Jane", "Fred"]
ages = [31, 35, 4]

for t in zip(names, ages):
    name = t[0]
    age = t[1]
    print(name, age)

for name, age in zip(names, ages):
    print(name, age)    

for i, name in enumerate(names):
    print(i, name)
    print(ages[i])