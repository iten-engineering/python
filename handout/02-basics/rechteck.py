
len = 10
witdh = 5

size = 2 * (len + witdh)
area = len * witdh

title = "Rechteck mit Länge " + str(len) + " und Breite " + str(witdh)

title2= f"Rechteck mit Länge {len} und Breite {witdh}"

title3= "Rechteck mit Länge {} und Breite {}".format(len, witdh)


print(title3)
print("- Umfang =", size)
print("- Fläche =", area)