
# Daten einlesen
in_filename = "handout/05-file/names.txt"
with open(in_filename, "r") as f:
    names = f.read().splitlines()

# Daten sortieren und anzeigen
names.sort()
print(names)

# Daten sortiert in Datei schreiben
out_filename = "handout/05-file/names-sorted.txt"
with open(out_filename, "w") as f:
    for name in names:
        f.write(name)
        f.write('\n')

with open(out_filename, "a") as f:
    f.write("Zorro")


