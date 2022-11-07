
def split_date(value):
    day, month, year = value.split(".")
    print("Date  :", value)
    print("day   :", day)
    print("month : {0=:02}".format(month))
    print("year  :", year)

split_date("17.04.1966")    
split_date("1.3.07")    
