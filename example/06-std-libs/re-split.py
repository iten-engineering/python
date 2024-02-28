import re

text = "Hello,World;how-are you"
expr = r"[,;\-\s]"

result = re.split(expr, text)
print(result)
