
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a_fruits = []

for fruit in fruits:
    if "a" in fruit:
        a_fruits.append(fruit)

print(a_fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits2 = [f for f in fruits if "a" in f]
print(fruits2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a_fruits = [fruit for fruit in fruits if "a" in fruit]
print(a_fruits)