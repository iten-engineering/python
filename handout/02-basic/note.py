
# Input section
value = input("Note = ")
print(value)

# Validate valid number
while (True):
    try:
        note = int(value)
        break
    except:
        print("Ungültiger Wert, die Eingabe ist keine Zahl.")
        value = input("Note = ")
        
# Validate range 1..6
if note < 1 or note > 6:
    print("Ungültiger Eingabebereich. Exit Programm!")
    exit(-1)

# Calculations
if note >=4:
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
    print("Note ungenügend.")