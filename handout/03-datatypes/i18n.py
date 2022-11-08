
greetings = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}

name = input("Geben sie bitte Ihren Namen ein: ")
lang = input("Wählen Sie die Sprache aus     : ")

key = lang if lang in greetings.keys() else "en"

print(greetings[key])
print(name)
