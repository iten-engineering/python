from datetime import datetime

class Person():

    def __init__(self, firstname, lastname, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

    def full_name(self):
        return self.firstname + " " + self.lastname

    def age(self):
        birthday_dt = datetime.strptime(self.birthday, "%d.%m.%Y")
        diff = datetime.now() - birthday_dt
        return diff.days/365

    def __str__(self):
        return self.full_name() + ", age:" + str(self.age())


# Application
persons = [
    Person("Pipi", "Langstrumpf", "15.10.1970"),
    Person("Peter", "Pan", "12.12.2012"),
    Person("Max", "Mortiz", "10.11.1966"),
]

for p in persons:
    print(p.full_name())
