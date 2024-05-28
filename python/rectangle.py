from figure import Figure

class Rectangle(Figure):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_name(self):
        return "Rectangle"

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width
