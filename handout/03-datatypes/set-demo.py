
names = ['Ivy', 'Charlie', 'Hank', 'Grace', 'Eva', 'David', 'Alice', 'Frank', 'Ivy', 'David', 'Charlie', 'Jack', 'Eva', 'Grace', 'Ivy', 'David', 'Hank', 'Frank', 'Charlie', 'Bob', 'Ivy', 'Alice', 'Charlie', 'David', 'Hank', 'Grace', 'Frank', 'Bob', 'Jack', 'Eva', 'Alice', 'Frank', 'Alice', 'Bob', 'Eva', 'Charlie', 'Hank', 'Alice', 'Ivy', 'Bob', 'Eva', 'Hank', 'Alice', 'Jack', 'Grace', 'Jack', 'David', 'Bob', 'Alice', 'Frank', 'Charlie', 'Ivy', 'David', 'Bob', 'Hank', 'Grace', 'Eva', 'Frank', 'Jack', 'David', 'Eva', 'Jack', 'Hank', 'Charlie', 'Ivy', 'Grace', 'Bob', 'Alice', 'Frank', 'Hank', 'Jack', 'Bob', 'Eva', 'Grace', 'David', 'Ivy', 'Charlie', 'Alice', 'Jack', 'Hank', 'Frank', 'Eva', 'Bob', 'Ivy', 'Grace', 'David', 'Alice', 'Charlie', 'Jack', 'Hank', 'Bob', 'Eva', 'Frank', 'Grace', 'David']
print(names)

unique_names = []
for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)

unique_names2 = set(names)
print(unique_names2)

name_count = {
    "Charlie": 10,
    "Sam": 0
}

name_count["Charlie"] = 22
print(name_count["Charlie"])


name_count["Anna"] = 0
print(name_count)
