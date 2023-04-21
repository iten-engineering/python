import re

pattern = r'\s+'

text = 'Hello\tworld\n\nfriday 123'
matches = re.findall(pattern, text)

print(matches)  # Output: ['\t', '\n\n']

text2 = re.sub(pattern, "-", text)
print(text2)

