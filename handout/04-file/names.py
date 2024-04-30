
in_file = "handout/04-file/names.txt"
out_file = "handout/04-file/names-sorted.txt"

with open(in_file, "r") as f:
    lines = f.read().splitlines()

print(lines)

lines.sort()

with open(out_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")