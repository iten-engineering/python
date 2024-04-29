
names = ["Peter", "Anna", "Sam"]

for i,name in enumerate(names):         # use enumerate and index
    print(i, name)


obj = enumerate(names)

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))