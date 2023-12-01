from datetime import datetime

class Person:

    def __init__(self, firstname, lastname, birthday, vip=False):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.vip = vip

    def fullname(self):
        return self.firstname + " " + self.lastname

    def age(self):
        birthday_datetime = datetime.strptime(self.birthday, "%d.%m.%Y")
        diff = datetime.now() - birthday_datetime
        age = diff.days / 365
        return age

    def __str__(self):
        return self.fullname() + ", Alter=" + str(self.age()) + ", VIP=" + str(self.vip)
    
persons = [
    Person("Pipi","Langstrumpf", "15.10.1970", vip=True),
    Person("Peter", "Pan", "12.12.2012"),
    Person("Max", "Moritz", "18.11.1966")
]

for person in persons:
    print( person )
