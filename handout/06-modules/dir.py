import os

path = os.getcwd()
entries = os.listdir(path)

print(path)
print(entries)

dirs = []
files = []

for entry in entries:
    entry_path = path + "/" + entry
    if os.path.isdir(entry_path):
        dirs.append(entry)
    else:
        files.append(entry)

print("Directories:")
for dir in dirs:
    print("-", dir)

print("Files:")
for file in files:
    print("-", file)
