# =============================================================================
# Python examples - standard library os
# =============================================================================

import os
print(dir(os))

demo_dir = "os-demo"

# Creating Directory
if not os.path.exists(demo_dir):
    os.mkdir(demo_dir)

# Changing the Current Working Directory
os.chdir(demo_dir)

print(os.getcwd())

# Create some files
open('fileA.txt', 'a').close()
open('fileB.txt', 'a').close()
open('fileC.txt', 'a').close()

# List Files and Sub-directories
print(os.listdir())




# =============================================================================
# The end.

