
i18n = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}

name = input("Geben sie bitte ihren Namen ein        : ")
key  = input("Wählen sie die Sprache [de, fr, it, en]: ")

key = key if key in i18n.keys() else "en"

# greeting = i18n.get(key)   # return None if key is invalid
greeting = i18n[key]         # raise Error if key is invalid  

print(greeting)
print(name)