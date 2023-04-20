
values = [7.5, 'Hello', 42, None, 'World', 1.25, 69, 12]

int_values = []
str_values = []
float_values = []

for v in values:
    if type(v) == int:
        int_values.append(v)
    elif type(v) == float:
        float_values.append(v)
    elif type(v) == str:
        str_values.append(v)

print(int_values)
print(float_values)
print(str_values)

x = None        # null in java
print(x)
