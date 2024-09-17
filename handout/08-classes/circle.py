import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius:{self.radius}"
    
    def area(self):
        return self.radius * 2 * math.pi

    def circumference(self):
        return self.radius * self.radius * math.pi

    def print(self):
        print("Kreis mit Radius:", self.radius)
        print("- Umfang =", self.circumference())
        print("- Fläche =", self.area())


circles = [Circle(4), Circle(7), Circle(9)]
for circle in circles:
    print(circle.radius)
    circle.print()

