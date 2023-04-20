
l = [1,2,3,4]
print(len(l))

if len(l) == 5:
    print("Die Länge ist 5:")
else:
    print("Die Länge ist", len(l))    


numbers = [1,2,3,4]
double_numbers = []
for n in numbers:
    double = n * 2
    double_numbers.append(double)    

print(numbers)
print(double_numbers)