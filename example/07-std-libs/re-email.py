import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

email = "example@example.com"
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
