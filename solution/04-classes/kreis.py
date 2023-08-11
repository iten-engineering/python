import math

class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        return 2 * math.pi * self.radius

    def flaeche(self):
        return math.pi * pow(self.radius,2)

    def print(self):
        print("Kreis mit Radius", self.radius)
        print("- Umfang =", self.umfang())
        print("- Fläche =", self.flaeche())


# Nur ausführen falls das Script direkt ausgeführt wird
# (wird nicht ausgeführt, wenn die Klasse  Circle von einem andere Modul benutzt wird).
if __name__ == '__main__':
    radien = [2,3,7,15]
    for radius in radien:
        k = Kreis(radius)
        k.print()

