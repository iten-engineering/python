
# Eingabe
input = input("Note = ")

# Validierung ungültige Eingabe
note = None
try:
    note = int(input)
except:
    print("Falscher Aufruf: Bitte übergeben Sie eine Zahl!")
    exit(-1)

# Validierung Zahlenbereich 1..6
if note < 1 or note > 6:
    print("Falscher Wert: Die Note muss einen Wert zwischen 1..6 haben!")
    exit(-2)

# Bestanden / nicht bestanden
if note >= 4:
    print("Der Test ist bestanden")
else:
    print("Der Test ist nicht bestanden")

# Detail Note
if note == 6:
    print("Note 6: sehr gut")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")
