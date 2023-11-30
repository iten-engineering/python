
name="Anna"
age=15


text = name + " ist " + str(age) + " Jahre alt."
print(text)

text2 = "{name} ist {age} Jahre alt.".format(age=age, name=name)
print(text2)

x = 5
text3 = "Ungültige Eingabe {nr}. Der Wert {nr} ist keine Gleitkommazahl!".format(nr=x)
print(text3)

