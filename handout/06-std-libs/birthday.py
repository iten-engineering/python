from datetime import datetime

now = datetime.now()
print(now)

birthday = datetime.strptime('01.03.2007', "%d.%m.%Y")
print(birthday)

age = now - birthday
print(age)
print(age.days / 365, "years")