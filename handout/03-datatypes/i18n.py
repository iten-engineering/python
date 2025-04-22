import json

"""
greetings = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}
"""

filename = "handout/03-datatypes/greetings.json"
with open(filename, 'r') as file:
    greetings = json.load(file)

name = input("Geben sie bitte Ihren Namen ein: ")
lang = input("Wählen sie die Sprache: ")

key = lang if lang in greetings.keys() else "en"
greeting = greetings[key]

print(greeting)
print(name)