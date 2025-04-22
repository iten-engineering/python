
person = {
    "firstnames": ["Michael", "Peter"],
    "lastname"  : "Bock",
    "address"   : {
        "street": "Bernstrasse 5",
        "zip"   : 3000,
        "city"  : "Bern"
    }
}


print(person['lastname'])
print(person['address'])
print(person['address']['zip'])

person['address']['zip'] = 3005
print(person['address']['zip'])
