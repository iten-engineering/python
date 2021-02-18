# =============================================================================
# Python examples - file input/output
# =============================================================================

# File input/output
# - f = open("path/to/file", "r")         # open a file for reading
# - f = open("path/to/file", "w")         # open a file for writing
# - f = open("path/to/file", "a")         # open a file for append
# - f.close()                             # close a file

# open with automatic close (with)
with open("hello.txt", "r") as f:
    text = f.read()
print(text)

# Read and write text
# - f.read()                              # read the whole file, give back a string
# - f.readline()                          # read the next line in the file
# - f.readlines()                         # read all lines in a file, give back a list
# - f.write("0,1\n1,2")                   # write into the file
# - f.writelines(["0,1","0,2"])           # write list of files

with open("test-numbers.txt", "w") as f:
    f.writelines(["1.0\n", "1.5\n", "2.0\n"])


# -----------------------------------------------------------------------------
# read and write csv with standard libraries
# -----------------------------------------------------------------------------
# - Das csv Modul funktioniert mit reader und writer Objekten (falls man das wirklich nutzen will)
# - Mit der Pandas Library (siehe weiter unten) steht eine "einfachere" Lösung zur Verfügung

import csv
titles = ["firstname", "lastname"]
rows   = [["Pipi", "Langstrumpf"], ["Peter", "Pan"], ["Marie", "Fischer"]]

with open("test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(titles)
    writer.writerows(rows)

data = []
with open("test.csv", "r") as f:
    reader = csv.reader(f)
    titles = reader.__next__()
    for row in reader:
        if (len(row) > 0):
            data.append(row)
print(data)

#
# read and write csv with pandas
#
import pandas

with open("test.csv", "r") as f:
    data_frame = pandas.read_csv(f)     # read a csv file

data_frame.index.name = "index"

with open("test-pandas.csv", "w") as f:
    data_frame.to_csv(f)                # write the data_frame to a csv file


# -----------------------------------------------------------------------------
# read and write objects
# -----------------------------------------------------------------------------
#- Pickle kann python Objekte speichern und lesen:

import pickle

d = {1:2, "k":[1,2,3], "fun":print}
print(d)

with open("test-dict.pkl", "wb") as fout:  # open file for write-binary
    pickle.dump(d, fout)                   # dump pickle file

with open("test-dict.pkl", "rb") as fin:   # open file for read-binary
    d2 = pickle.load(fin)                  # load pickle file
print(d2)

# =============================================================================
# The end.
