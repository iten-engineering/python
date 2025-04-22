
while(True):
    # Read data
    value = input("Note = ")
    # Check valid number
    try:
        note = int(value)
    except Exception as e:
        print("Einlesen der Note mit folgendem Fehler abgebrochen:", e)
        print("Bitte geben sie eine gültige Zahl ein.")
        continue
    # Check valid number range 1..6
    if note < 1 or note > 6:
        print("Ungültiger Zahlenbereich:", note)
        print("Bitte geben sie eine Zahl von 1-6 ein.")
        continue
    # Eingabe ist gültig
    break    

# Verarbeitung
if note < 4:
    print("Test ist leider nicht bestanden")
else:
    print("Test ist bestanden")

if note == 6:
    print("Note 6: sehr gut")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")

