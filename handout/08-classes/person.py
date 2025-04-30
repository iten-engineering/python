from datetime import datetime

class Person():

    def __init__(self, firstname, lastname, birthday, vip=False):
        self.fristname = firstname 
        self.lastname = lastname
        self.birthday = birthday
        self.vip = vip

    def fullname(self):
        return self.fristname + " " + self.lastname

    def age(self):
        birthday_dt = datetime.strptime(self.birthday, "%d.%m.%Y")
        age = datetime.now() - birthday_dt
        return age.days / 365

    def info(self):
        return f"{self.fullname()} ist {self.age():.0f} Jahre alt und vip={self.vip}"

    def __str__(self):
       return self.info()

persons = [
    Person("Lea", "Muster", "15.12.2001"),
    Person("Emilia", "Müller", "01.03.2007", vip=True),
    Person("Anna", "Baumann", "01.03.2017", vip=True)
]

for person in persons:
    print(person)

