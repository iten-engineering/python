import xmltodict

filename = "handout/04-file/persons.xml"

# Load the XML file as a dictionary
with open(filename, 'r') as xml_file:
    persons_dict = xmltodict.parse(xml_file.read())

# Access the list of persons
persons_list = persons_dict['persons']['person']

# Create E-Mail list
print("#")
print("# E-Mail list")
print("#")
for p in persons_list:
    firstname = p['firstname']
    lastname = p['lastname']
    email = p['contact']['email']
    print(firstname, lastname, email)


# Filter for females with age less than 30
print("#")
print("# Femals under 30 years")
print("#")
females_under_30 = [person for person in persons_list if person['gender'] == 'Female' and int(person['age']) < 30]

for p in females_under_30:
    firstname = p['firstname']
    lastname = p['lastname']
    age = p['age']
    print(firstname, lastname, age)
