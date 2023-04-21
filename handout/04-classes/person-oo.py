from datetime import datetime

class Person:
    """Die Klasse Person definiert alle Eigenschaften und Methoden einer Person."""

    def __init__(self, firstname, lastname, birthday, vip=False):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.vip = vip

    def full_name(self):
        return self.firstname + " " + self.lastname

    def age(self):
        birthday = self.birthday
        birthday_datetime = datetime.strptime(birthday, "%d.%m.%Y")
        diff = datetime.now() - birthday_datetime
        age = diff.days / 365
        return age

    def print_fullname_with_age(self):
        print(self.full_name(), ", age =", self.age(), ", vip=", self.vip )


persons = [
    Person("Pipi", "Langstrumpf", "15.10.1970"),
    Person("Peter", "Pan", "12.12.2012"),
    Person("Max", "Mortiz", "18.11.1966")
]

for p in persons:
    p.print_fullname_with_age()

robin = Person("Robin", "Müller", "12.05.2007")
robin.birthday = "01.01.2023"
robin.vip = True
robin.print_fullname_with_age()