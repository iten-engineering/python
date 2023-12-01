
in_file = "handout/04-file/names.txt"
out_file= "handout/04-file/sorted-names.txt"

with open(in_file, "r") as f:
    names = f.read().splitlines()

# names.sort()
sorted_names = sorted(names)

with open(out_file, "w") as f:
    for name in sorted_names:
        f.write(name)
        f.write('\n')

    
