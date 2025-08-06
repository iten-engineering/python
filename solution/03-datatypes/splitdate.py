
def show(date, day, month, year):
    print("Date:", date)
    print("  day   =", day)
    print("  month =", month)
    print("  year  =", year)

dates = ["17.04.1966", "1.3.07", "15.8.2021"]

print("--- Solution with split ---")
for date in dates:
    tokens = date.split(sep=".")
    day   = tokens[0]
    month = tokens[1]
    year  = tokens[2]
    show(date, day, month, year)

print("--- Solution with index und slicing ---")
for date in dates:
    idx1 = date.index(".")
    idx2 = date.index(".", idx1+1)
    day   = date[0:idx1]
    month = date[idx1+1:idx2]
    year  = date[idx2+1:]
    show(date, day, month, year)

