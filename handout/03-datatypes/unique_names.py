# File path to the text file
file_path = "handout/03-datatypes/names.txt"

# Step 1: Read the file and store names in a list
with open(file_path, "r") as file:
    names = file.read().splitlines()

print(names)

# Step 2: Create a set to remove duplicates and keep only unique names
unique_names_set = set(names)

# Step 3: Print the unique names
print("Unique Names:")
print(unique_names_set)
