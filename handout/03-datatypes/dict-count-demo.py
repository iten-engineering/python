names = ['Ivy', 'Charlie', 'Hank', 'Grace', 'Eva', 'David', 'Alice', 'Frank', 'Ivy', 'David', 'Charlie', 'Jack', 'Eva', 'Grace', 'Ivy', 'David', 'Hank', 'Frank', 'Charlie', 'Bob', 'Ivy', 'Alice', 'Charlie', 'David', 'Hank', 'Grace', 'Frank', 'Bob', 'Jack', 'Eva', 'Alice', 'Frank', 'Alice', 'Bob', 'Eva', 'Charlie', 'Hank', 'Alice', 'Ivy', 'Bob', 'Eva', 'Hank', 'Alice', 'Jack', 'Grace', 'Jack', 'David', 'Bob', 'Alice', 'Frank', 'Charlie', 'Ivy', 'David', 'Bob', 'Hank', 'Grace', 'Eva', 'Frank', 'Jack', 'David', 'Eva', 'Jack', 'Hank', 'Charlie', 'Ivy', 'Grace', 'Bob', 'Alice', 'Frank', 'Hank', 'Jack', 'Bob', 'Eva', 'Grace', 'David', 'Ivy', 'Charlie', 'Alice', 'Jack', 'Hank', 'Frank', 'Eva', 'Bob', 'Ivy', 'Grace', 'David', 'Alice', 'Charlie', 'Jack', 'Hank', 'Bob', 'Eva', 'Frank', 'Grace', 'David']

name_count = {}

for name in names:
    if name not in name_count.keys():
        name_count[name] = 1
    else:
        count = name_count[name]
        count = count + 1
        name_count[name] = count

print(name_count)