# =============================================================================
# Python examples - standard library json
# =============================================================================

import json

# -----------------------------------------------------------------------------
# json dump
# -----------------------------------------------------------------------------

# Sample data
data = {
    "name": "Jane Smith",
    "age": 25,
    "city": "Los Angeles"
}

# Open the JSON file for writing
with open('person.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been exported to 'person.json'.")

# -----------------------------------------------------------------------------
# json load
# -----------------------------------------------------------------------------

# Open the JSON file for reading
with open('person.json', 'r') as file:
    data = json.load(file)

# Access the data
print("Name:", data['name'])
print("Age:", data['age'])
print("City:", data['city'])

# =============================================================================
# The end.
