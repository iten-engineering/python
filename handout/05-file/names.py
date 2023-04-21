import os

print("Aktuelles Verzeichnis:")
print(os.getcwd())

in_file = "handout/05-file/names.txt"
out_file = "handout/05-file/names-sorted.txt"

with open(in_file, "r") as f:
    names = f.read().splitlines()

with open(out_file, "w") as f:
    for name in names:
        f.write(name)
        f.write('\n')
    



