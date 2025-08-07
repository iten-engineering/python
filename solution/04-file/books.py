import csv

path = "" # TODO set path according your installation
# path = "/home/lab/workspace/python-solution/05-file/";

# Read file content and save line to a list of lines:
in_file = path + "books.txt"
with open(in_file, "r") as f:
    lines = f.read().splitlines()       # get rid of '\n´


# Create list of book entries:
# - Each book entry is a list of: ISBN, Title, Author and Publisher
# - The first entry is the header line: ['ISBN', 'Title', 'Author', 'Publisher']
# - The other entries are the books   : ['978-0-316-45742-2', 'The Coast-To-Coast Murders', 'James Patterson', 'Little Brown USA']
books = []
book  = []
for line in lines:
    if line.strip() == "":
        books.append(book)
        book = []
    else:
        book.append(line.strip())

books.append(book)


# Create CSV file with titles and data rows:
titles = books[0]
rows = books[1:]

out_file = path + "books.csv"
print("Write data to:", out_file)
print("Titles:", titles)
print("Rows  :", rows)

with open(out_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(titles)
    writer.writerows(rows)

