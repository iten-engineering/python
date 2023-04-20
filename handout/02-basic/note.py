
value = input("Note = ")

# Validierung Eingabe Nummer
try:
    note = int(value)
except:
    print("Falsche Eingage, der Wert", value, "ist keine Nummer.")
    exit(-1)

# Validierung Note 1-6
if note < 1 or note > 6:
    print("Falsche Eingage, der Wert", value, "ist nicht zwichen 1 und 6.")
    exit(-2)

if note > 4:
    print("Test bestanden")
else:
    print("Test nicht bestanden")

if note == 6:
    print("Note 6: sehr gut")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")


