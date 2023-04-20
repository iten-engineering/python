
int_values = []
while True:
    value = input("Integer Wert = ")
    if value == "x":
        break
    try:
        int_value = int(value)
        int_values.append(int_value)
    except Exception as e:
        print("Ungültiger Wert:", value, ". Geben Sie bitte einen Integer ein.")
        print("Fehler:", str(e))

print("Werte:")
print(int_values)
