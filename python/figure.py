import math
from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, color: str):
        self.color = color

    def getColor(self):
        return self.color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass
