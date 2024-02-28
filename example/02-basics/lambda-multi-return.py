
mul = lambda x,y: x*y

result = mul(3,6)
print(result)

# Achtung: wir geben jetzt 2 Werte zurück!
add = lambda x,y: (print(x, "+", y, "=", x+y), x+y)

result = add(3,6)
print(result)