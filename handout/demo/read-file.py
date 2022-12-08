import csv

file = "handout/demo2/test.csv"

data = []
with open(file, "r") as f:
    reader = csv.reader(f)
    titles = reader.__next__()
    for row in reader:
        if (len(row) > 0):
            data.append(row)
print(data)



with open(file, "r") as f:
    reader = csv.reader(f)
    line = reader.__next__()
    while len(line) != 0:
        print(line)
        line = reader.__next__()


