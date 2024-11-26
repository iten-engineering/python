import os

print("Current working directory:")
print(os.getcwd())

NEW_LINE = "\n"

names_filename = "handout/04-file/names.txt"
sorted_names_filename = "handout/04-file/names-sorted.txt"

with open(names_filename, "r") as f:
    names = f.read().splitlines()

names.sort()

with open(sorted_names_filename, "w") as f:
    for name in names:
        f.write(name)
        f.write(NEW_LINE)

