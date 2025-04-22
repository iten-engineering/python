

numbers = []

while(True):
    # Read value
    value = input("Value = ")
    # Check exit
    if value == "x":
        break
    # Process value
    try:
        n = int(value)
        numbers.append(n)
    except:
        print("Invalid value")


print("Numbers:")
print(numbers)