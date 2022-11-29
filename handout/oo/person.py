from datetime import datetime

class Person:
    def __init__(self, firstname, lastname, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

    def fullname(self):
        return  self.firstname + " " + self.lastname

    def age(self):
        birthday = self.birthday
        birthday_dt = datetime.strptime(birthday, "%d.%m.%Y")
        diff = datetime.now() - birthday_dt
        age = diff.days / 365
        return age

    def print_fullname_with_age(self):
        print(self.fullname(), "age=", self.age())

    def __str__(self):
        return self.fullname()


persons = [
    Person("Max", "Moritz", "18.11.1966"), 
    Person("Pipi", "Langstrumpf", "15.10.1970")
]

for p in persons:
    print(p)

print(vars(persons[1]))