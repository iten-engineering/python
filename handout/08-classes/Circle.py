import math

class Kreis:

    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return math.pow(self.radius,2) * math.pi
    
    def umfang(self):
        return 2 * self.radius * math.pi
    
    def print(self):
        print(f"Kreis mit Radius {self.radius}")
        print(f"- Umfang = {self.umfang()}")
        print(f"- Fläche = {self.flaeche()}")        

radien = [3,7,6,8]
for r in radien:
    k = Kreis(r)
    k.print()