# =============================================================================
# Python examples - standard library re
# =============================================================================

import re
print(dir(re))

# -----------------------------------------------------------------------------
# findall()
# -----------------------------------------------------------------------------

# Print a list of all matches:
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# -----------------------------------------------------------------------------
# search()
# -----------------------------------------------------------------------------

# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# Make a search that returns no match:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# -----------------------------------------------------------------------------
# split()
# -----------------------------------------------------------------------------

# Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# -----------------------------------------------------------------------------
# sub()
# -----------------------------------------------------------------------------

# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# -----------------------------------------------------------------------------
# Match object
# -----------------------------------------------------------------------------

# Do a search that will return a Match Object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# The Match object has properties and methods used to retrieve information
# about the search, and the result:
#   .span() returns a tuple containing the start-, and end positions of the match.
#   .string returns the string passed into the function
#   .group() returns the part of the string where there was a match

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


# =============================================================================
# The end.

