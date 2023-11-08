# =============================================================================
# Python examples - standard library datetime
# =============================================================================

from datetime import date, datetime

# -----------------------------------------------------------------------------
# date
# -----------------------------------------------------------------------------

today = date.today()

print(today)
print(today.day, ".", today.month, ".", today.year, sep="")

today_str = date.strftime(today, "%d.%m.%Y")
print(today_str)

# -----------------------------------------------------------------------------
# datetime
# -----------------------------------------------------------------------------

now = datetime.now()
print(now)

birthday = datetime.strptime('01.03.2007', "%d.%m.%Y")
print(birthday)

age = now - birthday
print(age)
print(age.days / 365, "years")



# =============================================================================
# The end.

