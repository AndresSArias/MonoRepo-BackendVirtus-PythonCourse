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

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()


