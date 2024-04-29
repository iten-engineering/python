import xmltodict

filename = "handout/04-file/person.xml"

# Load the XML file and convert it to a dictionary
with open(filename, 'r') as f:
    xml_data = f.read()
    data_dict = xmltodict.parse(xml_data)

# Access the firstname and email values from the dictionary
firstname = data_dict['person']['firstname']
email = data_dict['person']['contact']['email']

# Print the values
print("Firstname:", firstname)
print("Email:", email)
