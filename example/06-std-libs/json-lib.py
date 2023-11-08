# =============================================================================
# Python examples - standard library json
# =============================================================================


{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}


import json

# Open the JSON file for reading
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the data
print("Name:", data['name'])
print("Age:", data['age'])
print("City:", data['city'])



import json

# Sample data
data = {
    "name": "Jane Smith",
    "age": 25,
    "city": "Los Angeles"
}

# Open the JSON file for writing
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been exported to 'output.json'.")





# =============================================================================
# The end.
