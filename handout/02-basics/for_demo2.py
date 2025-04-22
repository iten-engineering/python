
for i in range(0,10):
    # Bedingung prüfen
    if i % 2 == 1:
        continue
    # Verarbeitung
    # print(i)
        

numbers = [-5,7,-3,88,99,4]
find = 88


for i, n in enumerate(numbers):
    print("Check number:", n)
    if (n == find):
        print(i, n)
        break
