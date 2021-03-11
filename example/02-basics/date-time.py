# =============================================================================
# Python examples - date-time
# =============================================================================

# -----------------------------------------------------------------------------
# Import datetime from the datetime module and display the current date
# -----------------------------------------------------------------------------
from datetime import datetime

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)

# -----------------------------------------------------------------------------
# create datetime for a given date
# -----------------------------------------------------------------------------

birthdate = datetime(2007, 3, 1)
print(birthdate)

# -----------------------------------------------------------------------------
# formatting date objects into readable strings
# -----------------------------------------------------------------------------

# print day of week
print("Day  :", now.strftime("%A"))
print("Month:", now.strftime("%B"))

"""
Directive   Description                             Example 
    %a 	    Weekday, short version 	                Wed 	
    %A 	    Weekday, full version 	                Wednesday 	
    %w 	    Weekday as a number 0-6, 0 is Sunday 	3 	
    %d 	    Day of month 01-31 	                    31 	
    %b 	    Month name, short version 	            Dec 	
    %B 	    Month name, full version 	            December 	
    %m 	    Month as a number 01-12 	            12 	
    %y 	    Year, short version, without century 	18 	
    %Y 	    Year, full version 	                    2018 	
    %H 	    Hour 00-23 	                            17 	
    %I 	    Hour 00-12 	                            05 	
    %p 	    AM/PM 	                                PM 	
    %M 	    Minute 00-59 	                        41 	
    %S 	    Second 00-59 	                        08 	
    %f 	    Microsecond 000000-999999 	            548513 	
    %z 	    UTC offset 	                            +0100 	
    %Z 	    Timezone 	                            CST 	
    %j 	    Day number of year 001-366 	            365 	
    %U 	    Week number of year, Sunday first       52 	Sunday as the first day of week, 00-53
    %W 	    Week number of year, Monday first       52  Monday as the first day of week, 00-53 	
    %c 	    Local version of date and time 	        Mon Dec 31 17:41:00 2018 	
    %x 	    Local version of date 	                12/31/18 	
    %X 	    Local version of time 	                17:41:00 	
    %% 	    A % character 	                        % 	
    %G 	    ISO 8601 year 	                        2018 	
    %u 	    ISO 8601 weekday (1-7) 	                1 	
    %V 	    ISO 8601 weeknumber (01-53) 	        01
"""

# =============================================================================
# The end.

