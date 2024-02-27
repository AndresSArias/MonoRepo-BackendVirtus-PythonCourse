from models.circle import Circle
from models.square import Square
from models.triangle import Triangle


def main() :

    print('¿Qué figura desea crear?')
    print('1)Triangulo Equilatero')
    print('2)Cuadrado')
    print('3)Circulo')
    response =input('Seleccione un número: ')

    if (response == '1') :

        try:
            print('Escogió un triangulo equilatero')
            side = float(input('¿cuál es el lado del triangulo?'))
            height = float(input('¿cuál es el alto del triangulo?'))
            triangle = Triangle(side,height)
            triangle.calculateArea()
            triangle.calculatePerimeter()
            print(triangle)
        except Exception as e:
            print(f'Ocurrió un error de tipo {type(e)}, vuelva a ejecutar el programa.')

    elif (response == '2') :
        try:
            print('Escogió un cuadrado')
            side = float(input('¿cuál es el lado del cuadrado?'))
            square = Square(side)
            square.calculateArea()
            square.calculatePerimeter()
            print(square)
        except Exception as e:
            print(f'Ocurrió un error de tipo {type(e)}, vuelva a ejecutar el programa.')
    elif (response == '3'):
        try:
            print('Escogió un circulo')
            radius = float(input('¿cuál es el radio del cuadrado?'))
            circle = Circle(radius)
            circle.calculateArea()
            circle.calculatePerimeter()
            print(circle)
        except Exception as e:
            print(f'Ocurrió un error de tipo {type(e)}, vuelva a ejecutar el programa.')
    else:
        print('Error en la entrada, vuelva a ejecutar.')


if __name__ == '__main__':
    main()