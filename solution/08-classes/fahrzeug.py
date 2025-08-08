
class Fahrzeug:
    def __init__(self, typ, farbe, baujahr):
        self.typ = typ
        self.farbe = farbe
        self.baujahr = baujahr

    def fahren(self):
        print(self.typ, "fährt...")

    def to_string(self):
        return self.typ + " mit Farbe=" + self.farbe + ", Baujahr=" + str(self.baujahr)


class Fahrrad(Fahrzeug):
    def __init__(self, farbe, baujahr, marke):
        super().__init__("Fahrrad", farbe, baujahr)
        self.marke = marke

    def print(self):
        print(self.to_string() + ", Marke=" + self.marke)


class PKW(Fahrzeug):
    def __init__(self, farbe, baujahr, sitzplaetze):
        super().__init__("PKW", farbe, baujahr)
        self.sitzplaetze = sitzplaetze

    def print(self):
        print(self.to_string() + ", Sitzplätze=" + str(self.sitzplaetze))



if __name__ == '__main__':
    fahrrad = Fahrrad("silber", 2020, "Scott")
    fahrrad.print()
    fahrrad.fahren()
    pkw = PKW("rot", 2007, 4)
    pkw.print()
    pkw.fahren()

