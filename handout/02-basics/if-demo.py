
age = 12
gender = 'female'

print ("Start Verarbeitung")

print(age)
if age >= 18: 
    print("volljährig")
    if gender == 'male':
        print("male")
    else:
        print("female")
else:
    print("nicht volljährig")

print ("Ende Verarbeitung")

result = age == 12
print(result)


