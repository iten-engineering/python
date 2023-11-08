# =============================================================================
# Python examples - standard library datetime
# =============================================================================

from datetime import datetime, timedelta

def get_month_range(date):
    start_date = date.replace(day=1)
    next_month = start_date.replace(day=28) + timedelta(days=4)  # Ensure the next month is calculated correctly
    end_date = next_month - timedelta(days=next_month.day)
    return start_date, end_date

current_date = datetime.now()
start_of_month, end_of_month = get_month_range(current_date)

print("Start of month:", start_of_month.strftime('%Y-%m-%d'))
print("End of month:", end_of_month.strftime('%Y-%m-%d'))

print("Month ranges of 2023:")
for month in range(1,13):
    date_str = "01.{}.2023".format(month)
    date = datetime.strptime(date_str, "%d.%m.%Y").date()
    start_of_month, end_of_month = get_month_range(date)
    print(start_of_month, "...", end_of_month)    

# =============================================================================
# The end.
