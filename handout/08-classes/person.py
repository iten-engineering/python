from datetime import datetime

class Person():

    def __init__(self, firstname, lastname, birthday, vip=False):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.vip = vip

    def age(self):
        now_dt = datetime.now()
        birthday_dt = datetime.strptime(self.birthday, "%Y-%m-%d")
        age = now_dt - birthday_dt
        return int(age.days / 365)

    def fullname(self):
        return f"{self.firstname} {self.lastname} is vip={self.vip}"

    def __str__(self):
        return f"{self.fullname()} {self.age()} Jahre alt"


p1 = Person("Anna", "Müller", "2007-03-01")
p2 = Person("James", "Bond", "1966-04-21", vip=True)

persons = [p1, p2, Person("Max", "Müller", "1951-12-12")]

for p in persons:
    print(p)

