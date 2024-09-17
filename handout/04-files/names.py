

# filename = r"D:\dev\workspace\iten-engineering\python\handout\04-files\names.txt"
filename = "handout/04-files/names.txt"
filename_sorted = "handout/04-files/names-sorted.txt"

with open(filename, "r") as f:
    names = f.read().splitlines()

names.sort()
print(names)

# Alternative zu with:
try:
    f = open(filename_sorted, "w") 
    for name in names:
        f.write(name)
        f.write("\n")
finally:
    f.close()
