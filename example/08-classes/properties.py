class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def diameter(self):
        return 2 * self._radius

    def area(self):
        return 3.14 * self._radius ** 2

# Usage
c = Circle(5)
print("Radius:", c.radius)
print("Diameter:", c.diameter())
print("Area:", c.area())

# Changing radius using property setter
c.radius = 7
print("\nAfter updating radius:")
print("Radius:", c.radius)
print("Diameter:", c.diameter())
print("Area:", c.area())

# Trying to set invalid radius
try:
    c.radius = -2
except ValueError as e:
    print("\nError:", e)
