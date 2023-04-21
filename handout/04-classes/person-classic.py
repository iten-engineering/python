from datetime import datetime

# Daten zentral
persons = [
    {   "firstname": "Pipi",
        "lastname" : "Langstrumpf",
        "birthday" : "15.10.1970"
    },
    {   "firstname": "Peter",
        "lastname" : "Pan",
        "birthday" : "12.12.2012"
    },
    {   "firstname": "Max",
        "lastname" : "Mortiz",
        "birthday" : "18.11.1966"
    }
]

# Funktionen
def full_name(person):
    return person["firstname"] + " " + person["lastname"]

def age(person):
    birthday = person["birthday"]
    birthday_datetime = datetime.strptime(birthday, "%d.%m.%Y")
    diff = datetime.now() - birthday_datetime
    age = diff.days / 365
    return age

# Application
print("Persons:")
for p in persons:
    print( full_name(p), ", Alter=", age(p), "Jahre" )
