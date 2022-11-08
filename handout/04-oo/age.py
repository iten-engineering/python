from datetime import datetime

birthday = "17.04.1966"     # us date format: 04/17/1966 -> '%m/%d/%Y'
birthday_datetime = datetime.strptime(birthday, '%d.%m.%Y')

print(type(birthday_datetime))
print(birthday_datetime)            # printed in default format

diff = datetime.now() - birthday_datetime
print(type(diff))
print(diff)
print(diff.days / 365)