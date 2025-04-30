
filename = "handout/04-file/names.txt"
sorted_filename = "handout/04-file/names-sorted.txt"

with open(filename, "r") as f:
    names = f.read().splitlines()

names.sort()

with open(sorted_filename, "w") as f:
    for name in names:
        f.write(name)
        f.write("\n")
