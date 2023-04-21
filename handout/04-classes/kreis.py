
class Kreis:
    
    PI = 3.1415                         # statische Variable

    def __init__(self, radius):
        self.radius = radius            # Instanz Variable

    def umfang(self):
        return 2 * Kreis.PI * self.radius
    
    @staticmethod                       # statische Methode
    def get_pi():
        return Kreis.PI


print(Kreis.PI)
Kreis.get_pi()

radien = [1,5,7,9]
for r in radien:
    k = Kreis(r)
    print("Kreis mit Radius {} hat Umfang {}".format(k.radius, k.umfang()))