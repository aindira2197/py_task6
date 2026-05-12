import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(7)
print("Doira yuzi:", circle.area())
