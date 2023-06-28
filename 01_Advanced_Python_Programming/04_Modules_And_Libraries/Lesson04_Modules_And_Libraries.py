# Clase 4 Programacion Avanzada: Modulos

# En caso de que el fichero "misFunciones" se encuentre en la misma carpeta:
import myFunctions as mF #Importa todas las funciones del fichero/modulo
#from misFunciones import suma # De esta forma solo importamos lo que se especifica
#from misFunciones import * # De esta forma importamos todo y para inf¡vocarlo no hace falta escribir misFunciones.suma, solo con suma es suficiente

# En caso de estar en una subcarpeta:
#import subcarpeta.misFunciones

# En caso de querer acceder a un archivo fuera de la carpeta:
#import ../carpetaExterna.misFunciones #(no recomendable)

print(mF.suma(2,3))
print(mF.resta(2,3))

# Para consultar donde esta buscando python los paths:

import sys
print(sys.path)

#Add new path
#sys.path.append('ejemplo/de/ruta')

# Para consultar todos los modulos que tenemos cargados: te printa las funciones que puedes usar
print(dir())

# Para consultar el path del fichero
print(__file__)
print(mF.__file__)

# Para consultar el nombre del fichero
print(__name__)
print(mF.__name__)

