from datetime import datetime

class Person:
    """Class person, defines all attributes of a person and methods."""

    def __init__(self, firstname, lastname, birthday, vip=False):
        """Constructor for a person."""
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.vip = vip

    def fullname(self):
        return self.firstname + " " + self.lastname

    def age(self):
        birthday_datetime = datetime.strptime(self.birthday, '%d.%m.%Y')
        diff = datetime.now() - birthday_datetime
        age = diff.days / 365
        return age

    def print_fullname_with_age(self):
        print(self.fullname(), ", age =", self.age())

print("person.py: __name__ = ", __name__)

if __name__ == '__main__':
    print("### Meine Tests für die Klasse Person")
    p = Person("Pipi", "Langstrumpf", "15.10.1970", vip=True)
    p.print_fullname_with_age()