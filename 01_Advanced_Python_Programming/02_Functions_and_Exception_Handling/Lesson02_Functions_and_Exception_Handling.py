# Clase 2 Programacion Avanzada: Manejo de funciones


from typing import final


def nombre_funcion(argumentos):
    # code
    pass
    return

def suma(*numeros): # el asterisco indica un numero indeterminado de argumentos
    total = 0
    for i in numeros:
        total+= i
    return total

print(suma(1,2,3,4))

def suma(**numeros): # El doble asterisco indica que sera una lista de tuplas
    total = 0
    for i,j in numeros.items():
        print(i,j)
        total+= j
    return total

print(suma(a=2,b=3))

# Se pueden devolver varios parametros con el return

def sumayresta(a,b):
    return a+b,a-b

# Documentacion

def ejemplofuncion():
    '''
    Descripcion
    '''
    pass

# Excepciones: 
# raise y assert --> lo veremos mas adelante

# try y except

try:
    #lineas de codigo que queramos controlar
    a = 3
except ZeroDivisionError: # hay una serie de excepciones predefinidas
    print("detecta las divisiones entre 0")
except Exception as e: #tambien puedes no poner ninguna y definirlo tu, puedes capturar la excepcion y mostrarla
    print(f"ha ocurrido un error, el error {e}")
else:
    print("Se ejecutara si no ha ocurrido ninguna excepcion")
finally:
    print("Se ejecuta siempre")   


