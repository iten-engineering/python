
dates = ["17.04.1966","1.3.07", "15.8.2022"]

def show(date, day, month, year):
    print("Date   :", date)
    print(" day   =", day)
    print(" month =", month)
    print(" year  =", year)

for date in dates:
    tokens = date.split(".")
    d = tokens[0]
    m = tokens[1]
    y = tokens[2]
    show(date,d,m,y)

print("----------------------------")

def get_values():
    return 1, 2

x, y = get_values()
print(x, y)

print("----------------------------")

for date in dates:
    d,m,y = date.split(".")
    show(date,d,m,y)
