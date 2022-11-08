from datetime import datetime

# Daten Zentral
persons = [
    {  "firstname": "Pipi",
        "lastname" : "Langstrumpf",
        "birthday" : "15.10.1970"
    }, 
    {
        "firstname": "Peter",
        "lastname" : "Pan",
        "birthday" : "12.12.2012"
    }, 
    {
        "firstname": "Max",
        "lastname" : "Moritz",
        "birthday" : "18.11.1966"
    }
]

# Methoden
def full_name(person):
    return person["firstname"] + " " + person["lastname"]    

def age(person):
    birthday = person["birthday"]
    birthday_datetime = datetime.strptime(birthday, '%d.%m.%Y')
    diff = datetime.now() - birthday_datetime
    age = diff.days / 365
    return age

# Application
print("Persons:")
for person in persons:
    print( full_name(person), ", Alter =", age(person), "Jahre" )

