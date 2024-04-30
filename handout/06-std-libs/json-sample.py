import json

# Sample data
data = {
    "name": {
        "firstnames": ["Jane", "Anna"],
        "lastname": "Smith"
    },
    "age": 25,
    "city": "Los Angeles",
    "address": {
        "street": "Bernstrasse",
        "nr": 7,
        "city": "Basel",
        'country': None
    }
}

city = data['address']['city']
print( city )

file = 'handout/06-std-libs/person.json'

# Open the JSON file for writing
with open(file, 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been exported to 'person.json'.")
