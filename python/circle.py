from figure import Figure
import math

class Circle(Figure):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    def get_name(self):
        return "Circle"

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)
