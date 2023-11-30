names = ["Sam", "Mike", "Anna"]
ages = [12,18,25]
genders = ['male', 'male', 'female']

for name, age, gender in zip(names, ages, genders):
    print(name, age, gender)
