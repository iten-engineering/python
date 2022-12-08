
a = [1,2,3]
b = a
c = a.copy

b[0] = 11

print(id(a))
print(id(b))

print (a is b)
print (a is c)