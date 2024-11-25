print("Geben Sie bitte einen Integer ein oder 'x' um die Eingabe zu beenden:")

int_values = []
while(True):
    value = input("value = ")
    if value == "x":
        break
    try:
        int_value = int(value)
        int_values.append(int_value)
    except:
        print(f"Ungültige Eingabe {value}")

print("Eingegebene Werte:")
print(int_values)