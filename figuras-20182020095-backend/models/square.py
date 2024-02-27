from models.shape import Shape

class Square (Shape):

    def __init__(self, side):
        super().__init__()
        self._side = side
    
    @property
    def side (self):
        return self._side
    
    @side.setter
    def side (self,side):
        self._side = side

    def calculateArea (self):
        self._area = (self._side ** 2)


    def calculatePerimeter (self):
        self._perimeter = (self._side*4)

    def __str__(self):
        return f'El cuadrado con los lado de {self._side}u (cada uno) tiene un perímetro de {self._perimeter}u y un área de {self._area}u^2'