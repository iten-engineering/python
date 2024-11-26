import math

class Kreis:

    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        return self.radius * 2 * math.pi

    def flaeche(self):
        return math.pow(self.radius, 2) * math.pi

    def print(self):
        print("Kreis mit Radius", self.radius)
        print("- Umfang = ", self.umfang())
        print("- Fläche = ", self.flaeche())
    
    def __str__(self):
        return f"Kreis mit Radius {self.radius}"


radien = [5, 9, 15]
for radius in radien:
    k = Kreis(radius)
    k.print()
    print(k)