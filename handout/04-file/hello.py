import os

print(os.getcwd())
os.chdir(r"D:\dev\workspace\iten-engineering\python\handout\04-file")
print(os.getcwd())

# print(f"{os.getcwd()}\\handout\\04-file")

myfile = "hello.txt"

with open(myfile, "r") as f:
    text = f.read()

print(text)
