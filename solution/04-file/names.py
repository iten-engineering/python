
# read names
in_file = "names.txt"
with open(in_file, "r") as f:
    lines = f.read().splitlines()       # get rid of '\n´

# sort names
lines.sort()

# write sorted names
out_file = "names-sortet.txt"
print("Write data to:", out_file)
print(lines)

with open(out_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")

