from datetime import datetime

# Zentrale Daten
persons = [
    { "firstname": "Pipi",
      "lastname" : "Langstrumpf",
      "birthday" : "15.10.1970"
    },
    { "firstname": "Peter",
      "lastname" : "Pan",
      "birthday" : "12.12.2012"
    },
    { "firstname": "Max",
      "lastname" : "Moritz",
      "birthday" : "10.11.1966"
    }
]


# Methoden
def full_name(person):
    return person["firstname"] + " " + person["lastname"]

def age(person):
    birthday = person["birthday"]
    birthday_dt = datetime.strptime(birthday, "%d.%m.%Y")
    diff = datetime.now() - birthday_dt
    return diff.days/365


# Application
print("Personen:")
for person in persons:
    print( full_name(person), ", Alter:", age(person) )

