import json

i18n_file = "handout/05-file/i18n.json"

i18n = {
    "de": "Guten morgen",
    "fr": "Bon jour",
    "it": "Buongiorno",
    "en": "Good morning"
}

with open(i18n_file, "w") as f:
    json.dump(i18n, f)

with open(i18n_file, "r") as f:
    d = json.load(f)

print("Greetings loaded from json file:")
print(d)


