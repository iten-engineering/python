import json

filename = "handout/03-datatypes/i18n.json"

"""
greetings = {
    "de" : "Guten morgen",
    "fr" : "Bon jour",
    "it" : "Buongiorno",
    "en" : "Good morning"
}


with open(filename, "w") as f:
    json.dump(greetings, f)
"""

with open(filename, "r") as f:
    greetings = json.load(f)


name = input("Geben sie bitte ihren Namen ein    : ")
lang = input("Wälen sie die Sprache [de,fr,it,en]: ")

key = lang if lang in greetings.keys() else "en"
greeting = greetings[key]

print(greeting)
print(name)