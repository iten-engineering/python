
i18n = {
    "de": "Guten morgen",
    "fr": "Bonjour",
    "it": "Buongiorno",
    "en": "Good morining"
}

name = input("Geben sie bitte ihren Namen ein: ")
key = input("Geben Sie die Sprache an [de, fr, it, en]: ")

key = key if key in i18n.keys() else "en" 
greeting = i18n.get(key)

print(greeting)
print(name)
