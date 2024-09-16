
# gerade oder ungerade Zahl
print( 4 % 2 == 0)
print( 5 % 2 == 0)


numbers = [5, 12, -7, 22, "x", 4, 8]
for n in numbers:
    if n == "x":
        break   
    if (n % 2 == 1):    # ungerade zahl
        continue    
    print(n)


