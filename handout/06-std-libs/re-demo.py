import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(pattern, email) else False

valid_emails = ["example@example.com", "t.huber@gmx.ch"]
invalid_emails = ["t@@company.ch", "@ubs.ch"]

print("Gültige E-Mail:")
for email in valid_emails:
    result = validate_email(email)
    print(email, result)

print("Ungültige E-Mail:")
for email in invalid_emails:
    result = validate_email(email)
    print(email, result)

