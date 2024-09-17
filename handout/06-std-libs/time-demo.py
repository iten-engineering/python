import datetime
import time

# Get the current time in seconds since the epoch (1970-01-01)
current_time_seconds = time.time()

# Define the epoch start time (1970-01-01)
epoch_start = datetime.datetime(1970, 1, 1)

# Convert seconds since the epoch to a datetime object
current_time = datetime.datetime.fromtimestamp(current_time_seconds)

# Calculate the time difference (timedelta) between now and the epoch start
elapsed_time = current_time - epoch_start

# Display the elapsed time as a timedelta object
print(f"Elapsed time since 1970-01-01: {elapsed_time}")
print(f"Total days: {elapsed_time.days}, Total seconds: {elapsed_time.seconds}, Total microseconds: {elapsed_time.microseconds}")
