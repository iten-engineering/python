

input_count = 0

while True:
    try:
        # check input count
        if input_count >= 3:
            print(f"Anzahl Eingabeversuche {input_count} überschritten")
            exit()
        input_count = input_count + 1
        # check valid number
        value = input("Note = ")       
        note = int(value)
        # check valid number range
        if note < 1 or note > 6:
            print(f"Die Eingabe ist ungültig, die Note {note} ist nicht zwischen 1-6.")
            continue
        # erfolgreiche Note zwischen 1-6 eingelesen
        break
    except Exception as e:
        print(f"Die Eingabe ist ungültig, der Wert {value} ist keine Ganzzahl.")
        print("Fehler:", e)


if note >= 4:
    print("Test bestanden")
else:
    print("Test leider nicht bestanden")

if note == 6:
    print("Note 6: sehr gut")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")

