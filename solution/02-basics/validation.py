

print("Geben Sie bitte einen Integer ein oder 'x' um die Eingabe zu beenden:")

numbers = []
while (True):
    try:
        value = input("value = ")
        if (value == "x"):
            break;
        number = int(value)
        numbers.append(number)
    except:
        print("Ungültiger Wert:", value, "Geben Sie bitte einen Integer Wert ein!")

print("\nEingegebene Werte:")
print(numbers)
