from calculadora import * 

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")

try:
    option = int(option)
except:
    print ("valor no valido")
    exit()

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()

def validateNumber (text):
    try:
        return float(input(text))
    except:
        print ("valor no valido")
        exit()


def main ():
    a = None
    b = None

    if (option == 1):
        print(f'Ha seleccionado {option}, lo que es una suma. Por favor:\n')
        a = validateNumber ('Ingrese el valor del sumando a: ')
        b = validateNumber ('Ingrese el valor del sumando b: ')
        print(f'El valor de la suma es: {suma(a,b)}')
    elif (option == 2):
        print(f'Ha seleccionado {option}, lo que es una resta. Por favor:\n')
        a = validateNumber ('Ingrese el valor del minuendo a: ')
        b = validateNumber ('Ingrese el valor del sustraendo b: ')
        print(f'El valor de la resta es: {resta(a,b)}')
    else:
        print(f'Ha seleccionado {option}, lo que es una divisón. Por favor:\n')
        a = validateNumber ('Ingrese el valor del dividendo a: ')
        b = validateNumber ('Ingrese el valor del divisor b: ')
        print(f'El valor de la división es: {resta(a,b)}')        

if __name__ == '__main__':
    main()
