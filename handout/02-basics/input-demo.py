
def input_zahl(prompt):
    value = input(prompt)
    return float(value)

value = input_zahl("Number = ")
print(value, type(value))