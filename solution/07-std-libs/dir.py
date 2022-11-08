import os

path = os.getcwd()
entries = os.listdir(path)

dirs = []
files = []
for entry in entries:
    entry_path = path + "/" + entry
    if os.path.isdir(entry_path):
        dirs.append(entry)
    else:
        files.append(entry)

print("Directories:")
for d in dirs:
    print("-", d)

print("Files:")
for f in files:
    print("-", f)
