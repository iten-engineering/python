from datetime import datetime

# Daten Zentral
persons = [
    { "firstname": "Pipi",  "lastname": "Langstrumpf", "birthday":"15.10.1970" },
    { "firstname": "Peter", "lastname": "Pan",         "birthday":"12.12.2012" },
    { "firstname": "Max",   "lastname": "Moritz",      "birthday":"18.11.1966" }
]

def fullname(person):
    return f"{person['firstname']} {person['lastname']}"

def age(person):
    birthday = person['birthday']
    birthday_datetime = datetime.strptime(birthday, "%d.%m.%Y")
    diff = datetime.now() - birthday_datetime
    age = diff.days / 365
    return age

def fullname_with_age(person):
    return f"{fullname(person)} mit Alter: {age(person)}"

# Anwendung
print("Person List:")
for p in persons:
    print(fullname_with_age(p))
