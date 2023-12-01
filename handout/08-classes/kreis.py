import math

class Kreis:

    def __init__(self, radius):
        self.radius = radius

    def get_umfang(self):
        return self.radius * 2 * math.pi

    def get_flaeche(self):
        return math.pi * self.radius**2
    
    def print(self):
        print("Kreis mit Radius:", self.radius)
        print("- Umfang =", self.get_umfang() )
        print("- Fläche =", self.get_flaeche() )

k = Kreis(5)
k2 = Kreis(7)

k.print()
k2.print()