
print("Hello", "World", sep="_")

print("Hello", end=" ")
print("World")

# Open the file in write mode
filename = "handout/04-files/output.txt"
with open(filename, 'w') as file:
    # Print to the file
    print("Hello, World!", file=file)
