names = ["Peter", "Jane", "Fred"]
ages = [31, 35, 4, 3]

if len(names) != len(ages):
    raise Exception("Listen sind ungleich gross")

for t in zip(names, ages):              # use a tuple
    print(t)
