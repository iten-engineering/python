
words = ["winter", "is", "coming"]
for w in words:
    print(w)


numbers = [1, -5, 12, 99, -77, 100]
for n in numbers:
    # bedingung prüfen
    if n < 0:
        continue
    # verarbietung
    print(n)
    if n < 10:
        print("kleine Zahl")
    elif n >=10 and n < 20:
        print("mittlere Zahl")
    else:
        print("grosse Zahl")    
    




print("next")

