
text = "this and that"
search = "th"

first_pos = text.find("th")       		
last_pos = text.rfind(search)




print(f"Erste  Position von '{search}': {first_pos}")
print(f"Letzte Position von '{search}': {last_pos}")