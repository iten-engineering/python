

#rest = 4 % 2
#print(rest)


for i in range(1,11):
    rest = i % 2
    ist_gerade = (rest == 0)

    if ist_gerade:
        ist_gerade_de = "Ja"
    else:
        ist_gerade_de = "Nein"

    print(i, "gerade Zahl:", ist_gerade_de)