from models.shape import Shape


class Triangle (Shape):

    def __init__(self, side,height):
        super().__init__()
        self._side = side
        self._height = height
    
    @property
    def side (self):
        return self._side
    
    @side.setter
    def side (self,side):
        self._side = side

    @property
    def height (self):
        return self._height
    
    @height.setter
    def height (self, height):
        self._height = height

    def calculateArea (self):
        self._area = (self._side * self._height)/2


    def calculatePerimeter (self):
        self._perimeter = (self._side*3)

    def __str__(self):
        return f'El triangulo equilatero con lado {self._side}u y altura de {self._height}u tiene un perímetro de {self._perimeter}u y un área de {self._area}u^2'