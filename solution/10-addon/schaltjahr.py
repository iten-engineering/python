
value = input("Geben Sie bitte eine Jahreszahl ein: ")

year = int(value)
leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    else:
        leap_year = True

if leap_year:
    print("Das Jahr", year, "ist ein Schaltjahr")
else:
    print("Das Jahr", year, "ist KEIN Schaltjahr")
