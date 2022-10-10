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

# start_path = "/home/lab/workspace/python-solution/09-apps/"
start_path = "D:/dev/surfmachine/python/solution/09-apps/"
dir_walker(start_path, 0)


