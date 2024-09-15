# =============================================================================
# Python examples - match case (since Python 3.10)
#
# Reference:
# - https://codefinity.com/blog/Match-case-Operators-in-Python
# =============================================================================

# Print a message, depending on the day of the week
day = "Monday"

match day:
    case "Monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday!")
    case "Wednesday":
        print("It's Wednesday!")
    case _:
        print("It's not Monday, Tuesday, or Wednesday.")

# =============================================================================
# The end.