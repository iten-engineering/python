
from datetime import datetime

class Person():

    def __init__(self, firstname, lastname, age=None):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = age

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def age(self):
        if self.birthday is None:
            return "unbekannt"
        birthday_datetime = datetime.strptime(self.birthday, "%d.%m.%Y")
        diff = datetime.now() - birthday_datetime
        age = diff.days / 365
        return age
    
    def fullname_with_age(self):
        return f"{self.fullname()} mit Alter: {self.age()}"


persons = [
    Person("Pipi", "Langstrumpf", age="15.07.2011"),
    Person("Peter", "Pan", age="12.12.2012"),
    Person("Max", "Moritz")
]

# Anwendung
print("Person List:")
for p in persons:
    print(p.fullname_with_age())
