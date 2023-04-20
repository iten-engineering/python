
names = ["Peter", "Jane", "Fred"]
ages = [31, 35, 25]
gender = ["male", "female", "male"]

for t in zip(names, ages):
    print(t)

for name, age, g in zip(names, ages, gender):
    print(name, "ist ", age, " Jahre alt mit Geschlecht:", g)
