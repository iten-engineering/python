
value = input("Note = ")
try:
    note = int(value)
except:
    print(f"Ungültige Eingabe: [{value}] ist keine Ganzzahl!")
    exit(1)

if note < 1 or note > 6:
    print("Ungültiger Zahlenbereich.")
    exit(1)

if note >= 4:
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
    print(f"Note {note}: ungeügend")

