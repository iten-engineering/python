
numbers = []

while(True):
    try:
        value = input("Eingabe = ")
        if value == "x":
            break
        number = int(value)
        numbers.append(number)
    except:
        print(f"Ungültige Eingabe {value} ist kein Integer.")

print(numbers)

