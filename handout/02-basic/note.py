
note = None

while note is None:
    # Prüfung Eingabe auf Integer
    try:
        value = input("Note = ")
        note = int(value)
    except:
        message = f"Ungültige Eingabe, der Wert '{value}' ist kein Integer." 
        print(message)
    # Prüfung Zahlenbereich 1..6
    if note < 1 or note > 6:
        message = f"Ungültiger Wert, '{note}' ist ausserhalb 1-6." 
        print(message)
        note = None

if note >= 4:
    print("Test bestanden")
else:
    print("Test leider nicht bestanden")

if note == 6:
    print("Note 6: ausgezeichnet")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")    