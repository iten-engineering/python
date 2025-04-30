import os

cwd = os.getcwd()
print(cwd)

files = []
directories = []

entries = os.listdir()

for entry in entries:
    fn = cwd + "/" + entry
    
    if (os.path.isdir(fn)):
        directories.append(entry)
    
    if (os.path.isfile(fn)):
        files.append(entry)
    

print("Verzeichnisse:")
print(directories)

print("Dateien:")
print(files)

