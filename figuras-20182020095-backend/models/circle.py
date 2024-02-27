import math
from models.shape import Shape


class Circle (Shape):

    def __init__(self, radius):
        super().__init__()
        self._radius = radius
    
    @property
    def radius (self):
        return self._radius
    
    @radius.setter
    def radius (self,radius):
        self._radius = radius

    def calculateArea (self):
        self._area = math.pi * (self._radius ** 2)


    def calculatePerimeter (self):
        self._perimeter = (self._radius*2*math.pi)

    def __str__(self):
        return f'El circulo con el radio de {self._radius}u tiene un perímetro de {self._perimeter}u y un área de {self._area}u^2'