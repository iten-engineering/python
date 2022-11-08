from person import Person

persons = [
    Person("Pipi", "Langstrumpf", "15.10.1970", vip=True),
    Person("Peter","Pan","12.12.2012"),        
    Person("Max","Moritz","18.11.1966")        
]

# Application
print("Persons:")
for person in persons:
    person.print_fullname_with_age()

