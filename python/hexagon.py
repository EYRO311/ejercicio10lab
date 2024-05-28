from figure import Figure
import math

class Hexagon(Figure):
    def __init__(self, color: str, side: float):
        super().__init__(color)
        self.side = side

    def get_name(self):
        return "Hexagon"

    def perimeter(self):
        return 6 * self.side

    def area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2
