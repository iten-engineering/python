greetings = {
    "de": "Guten morgen",
    "fr": "Bon jour", 
    "it": "Buongiorno",
    "en": "Good morning"
}

name = input("Name = ")
key = input("Sprachcode = ")

key = key if key in greetings.keys() else "en"

greeting = greetings[key]
print(greeting)
print(name)