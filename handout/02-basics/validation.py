
print("Geben Sie bitte einen Integer ein oder 'x' um die Eingabe zu beenden:")
values = []

value = input("value = ")
while value != 'x':
    try:
        int_value = int(value)
        values.append(int_value)
    except:
        print("Ungültiger Wert:", value)
    value = input("value = ")

print("Integers:")
print(values)
