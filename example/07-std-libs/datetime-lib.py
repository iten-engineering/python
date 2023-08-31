# =============================================================================
# Python examples - standard library datetime
# =============================================================================

from datetime import date, datetime

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

today_str = date.strftime(today, "%d.%m.%Y")
print(today_str)

birthday = datetime.strptime('01.03.2007', "%d.%m.%Y").date()
print(birthday)

age = today - birthday
print(age)
print(age.days / 365)

# =============================================================================
# The end.

