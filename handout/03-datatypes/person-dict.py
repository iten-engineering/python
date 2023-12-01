person = {
    "firstnames": ["Peter","Thomas"],
    "lastname"  : "Meier",
    "address"   : {
        "street": "Bernstrasse",
        "nr"    : 25,
        "zip"   : 3000,
        "city"  : "Bern"
    }
}

print(person["firstnames"])
print(person["lastname"])
print(person["address"]["city"])