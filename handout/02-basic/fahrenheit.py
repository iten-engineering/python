
value = input("Temperatur in Fahrenheit:")
print(value)
print(type(value))

fahrenheit = float(value)
# print(fahrenheit)
# print(type(fahrenheit))

celsius = 5 * (fahrenheit - 32) / 9

print("Temperatur:")
print("Fahrenheit =", fahrenheit)
print("Celsius    =", celsius)



