
text = "anna peter mike eva"
print(text)

words= text.split()
cwords = []
for w in words:
    cw = w.capitalize()
    cwords.append(cw)

ctext = " ".join(cwords)
print(ctext)


