import xmltodict

file = "handout/04-file/person.xml"

# Load the XML file and convert it to a dictionary
with open(file, 'r') as f:
    xml_data = f.read()
    data_dict = xmltodict.parse(xml_data)

# Access the firstname and email values from the dictionary
firstnames = data_dict['person']['firstname']
emails = data_dict['person']['contact']['email']

# Print the values
print("Firstname:", firstnames)
print("Email:", emails)
