from Kreis import Kreis

class Zylinder(Kreis):
    def __init__(self, radius, hoehe):
        super().__init__(radius)
        self.hoehe = hoehe

    def volumen(self):
        return self.flaeche() * self.hoehe

    def print(self):
        print("Zylinder mit Radius", self.radius, "und Höhe", self.hoehe)
        print("- Volumen =", self.volumen())


if __name__ == '__main__':
    k = Kreis(3)
    k.print()
    z = Zylinder(3, 5)
    z.print()