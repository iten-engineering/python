
i18n = {
    "de" : "Guten morgen",
    "fr" : "Bon jour",
    "it" : "Buongiorno",
    "en" : "Good morning"
}

name = input("Geben Sie bitte Ihren Namen ein: ")
key = input("Wählen Sie die Sprache [de, fr, it, en]: ")

# check if key is available
key = key if key in i18n.keys() else "en"

# greeting
greeting = i18n[key]
print(greeting)
print(name)

