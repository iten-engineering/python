
reading = True

while(reading):
    try:
        value = input("Temperatur in Fahrenheit = ")
        fahrenheit = float(value)
        reading = False
    except Exception as e:
        print(f"Falsche Eingabe [{value}], Fahrenheit ist keine Zahl")

celsius = 5 * (fahrenheit - 32) / 9


print("Fahrenheit =", fahrenheit)
print("Celsius    =", celsius)