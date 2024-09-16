import json

"""
i18n = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}
"""

i18n_file = "handout/03-datatypes/i18n.json"

with open(i18n_file, 'r') as json_file:
    i18n = json.load(json_file)

print(i18n["de"])
print(i18n["en"])

name = input("Name = ")
lang  = input("Sprachcode = ")

key = lang if lang in i18n.keys() else "en"
greeting = i18n[key]

print(greeting)
print(name)