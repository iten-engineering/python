
valid_numbers = []
invalid_inputs = []

"""
run = True
while(run):
    try:
        value = input("Eingabe Nummer:")   
        if value == 'x':
            run = False
        else:
            number = int(value)
            valid_numbers.append(number)
    except:
        print("Ungültiger Wert:", value)
        invalid_inputs.append(value)
"""

while(True):
    try:
        value = input("Eingabe Nummer:")   
        if value == 'x':
            break
        number = int(value)
        valid_numbers.append(number)
    except:
        print("Ungültiger Wert:", value)
        invalid_inputs.append(value)

print()
print("Ungültige Eingaben:")
print(invalid_inputs)

print("Gültige Nummern:")
print(valid_numbers)

