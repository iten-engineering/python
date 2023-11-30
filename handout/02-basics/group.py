x = None

print(type(x))

if x is None:
    print("x ist noch nicht initalisiert")
else:
    print(x)

values  = [7.5, 'Hello', 42, None, 'World', 1.25, 69, 12]

int_values = []
float_values = []
str_values = []

for value in values:
    print(value, type(value))
    if type(value) == int:
        int_values.append(value)
    elif isinstance(value, float):
        float_values.append(value)
    elif isinstance(value, str):
        str_values.append(value)


print(int_values)
print(float_values)
print(str_values)