import re

pattern = r'\s+'

text = 'Hello\tworld\n\nfriday 123'
matches = re.findall(pattern, text)

print(matches)  # Output: ['\t', '\n\n']

text2 = re.sub(pattern, "-", text)
print(text2)


# E-Mail
def is_valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email) is not None

tests = [
    "x.y@test.com",
    "x.y@test"
]

for test in tests:
    result = is_valid_email(test)
    print(test, result)