fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for fruit in fruits: 
    if "a" in fruit: 
        newlist.append(fruit)

print(fruits)
print(newlist)


# List Comprehension

newlist2 = [fruit for fruit in fruits if "a" in fruit] 
print(newlist2)