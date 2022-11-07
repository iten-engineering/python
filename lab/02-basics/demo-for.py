
words = ["winter", "is", "comming"]

for w in words:
    print(w)
print()

# break

namen = ["Anna", "Sam", "Beat", "Sam", "Eva"]

for name in namen:
    print(name)
    if name == "Sam":
        break
print("---")

for name in namen:
    if name != "Sam":
        continue
    print("Sam gefunden")



