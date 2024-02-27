from abc import ABC
from abc import abstractmethod

class Shape (ABC) :

    def __init__(self):
        self._perimeter = None
        self._area = None

    @property
    def perimeter (self):
        return self._perimeter
    
    @perimeter.setter
    def perimeter (self, perimeter):
        self._perimeter = perimeter
    
    @property
    def area (self):
        return self._area
    
    @area.setter
    def area (self, area):
        self._area = area

    @abstractmethod
    def calculateArea (self):
        pass

    @abstractmethod
    def calculatePerimeter (self):
        pass