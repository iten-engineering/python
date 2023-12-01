
i18n = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}

name = input("Geben sie bitte ihren Namen ein: ")
key  = input("Geben sie den Sprachcode ein   : ")

if key not in i18n.keys():
    key = "en"

greeting = i18n.get(key)

print(greeting)
print(name)

