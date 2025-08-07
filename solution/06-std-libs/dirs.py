import os

def dir_walker(path, level):
    content = os.listdir(path)
    dirs  = [el for el in content if os.path.isdir(path + el)]
    files = [el for el in content if os.path.isfile(path + el)]
    intend = " " * (level*2)
    for file in files:
        print(intend + file)
    for dir in dirs:
        print(intend + dir)
        dir_walker(path + dir + "/", level+1)

start_path = os.getcwd() + "\\solution\\"

print("#")
print("# start_path")
print("#")
print(start_path)

print("#")
print("# tree")
print("#")
dir_walker(start_path, 0)


