

def create_custmor(firstname, lastname, birthdate=None):
    if birthdate is None:
        print("Create customer firstname={}, lastname={}".format(firstname, lastname) )
    else:
        print("Create customer firstname={}, lastname={}, birthdate={}".format(firstname, lastname, birthdate) )

create_custmor("Peter", "Pan")
create_custmor("Pipi", "Langstrumpf", birthdate="25.08.1966")

def draw_box(length, width, color="black", fill="white"):
    print("draw box:", length, "x", width, "color =", color, "fill =", fill)

draculaTheme = {
    "color":  "red",
    "fill": "black"
}
defaultTheme = {
    "color":  "gray",
    "fill": "white"
}
box1 = [3,6]
box2 = [2,12]

draw_box(*box1, **draculaTheme)
draw_box(*box2, **defaultTheme)


