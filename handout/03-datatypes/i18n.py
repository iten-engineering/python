
greetings = {
    "de" : "Guten morgen",
    "fr" : "Bon jour",
    "it" : "Buongiorno",
    "en" : "Good morning"
}

name = input("Geben sie bitte ihren Namen ein    : ")
lang = input("Wälen sie die Sprache [de,fr,it,en]: ")

key = lang if lang in greetings.keys() else "en"
greeting = greetings[key]

print(greeting)
print(name)