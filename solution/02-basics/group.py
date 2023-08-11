
values = [7.5, "Hello", 42, None, "World", 1.25, 69, 12]

int_values = []
float_values = []
str_values = []

for value in values:
    if type(value) == int:
        int_values.append(value)
    elif type(value) == float:
        float_values.append(value)
    elif type(value)==str:
        str_values.append(value)

print("values  =", values)
print("- int   =", int_values)
print("- float =", float_values)
print("- str   =", str_values)