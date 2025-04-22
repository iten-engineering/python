
read_data = True

numbers = []


while(read_data):
    value = input("Value = ")
    if value == "x":
        read_data = False
    else:
        try:
            n = int(value)
            numbers.append(n)
        except:
            print("Invalid value")


print("Numbers:")
print(numbers)