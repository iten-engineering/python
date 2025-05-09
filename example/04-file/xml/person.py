import xmltodict

filename = "example/04-file/xml/person.xml"

# Load the XML file and convert it to a dictionary
with open(filename, 'r') as f:
    xml_data = f.read()
    data_dict = xmltodict.parse(xml_data)

# Show dictionary
print(data_dict)

# Access the firstname and email values from the dictionary
firstname = data_dict['person']['firstname']
email = data_dict['person']['contact']['email']
vip = data_dict['person']['@vip']

# Print the values
print("Firstname:", firstname)
print("Email:", email)
print("VIP:", vip)

