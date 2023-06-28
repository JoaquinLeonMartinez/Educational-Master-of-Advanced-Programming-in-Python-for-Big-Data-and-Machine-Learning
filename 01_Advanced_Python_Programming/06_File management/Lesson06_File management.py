# Clase 6 Programacion Avanzada: Tratamiento de ficheros

# Abriendo el fichero
fichero = open("test.txt")

# Lectura de fichero
#print(fichero.read()) # Printa todo el fichero

#print(fichero.readline()) # Printa una linea
#print(fichero.readline(5)) # Printa el numero de caracteres de la linea que indiques

# Otra forma de leer las lineas:
lineas = fichero.readlines()

#print(lineas) # Esto no tira del todo porque es realmente un array de lineas, para leerlo debe ser con un bucle
'''
for linea in lineas:
    print(linea)
''' 
fichero.close()

'''
Argumentos de la funcion open():
r: por defecto, para leer el fichero
w: para escribir en el fichero
x: para crearlo, falla si ya existe
a: para añadir contenido a un fichero que ya existe
b: para abrir un fichero en modo binario
'''

fichero = open("test.txt", 'r')
lineas = fichero.readlines()
print(lineas)
fichero.close()

# Tratamiento de excepciones en fichero

fichero = open("test.txt")
try:
    pass
finally:
    fichero.close()

# With fichero:
with open("test.txt") as fichero:
    fichero.readlines() 
    # Cuando utilizas with no hace falta indicar el close() al final ya que se cierra automaticamente

''' 
excritura de ficheros:

w: Borra en caso de que exista y crea uno nuevo
a: añade contenido al fial del fichero si ya existe
x: en caso de existir el fichero nos devuelve error

'''

#fichero = open("miTest.txt", 'a')
fichero = open("myTest.txt", 'w') # Para testear mejor lo vamos borrando en cada ejecucion


fichero.write("nueva liena bb")

lista = ["linea en lista","y otra mas!","y otra!"]

for aux in lista:
    fichero.write(aux + '\n') #OJO! esto no mete saltos de linea, se mete todo en la misma linea si no se lo indicas

fichero.close()

# writeLineas:
fichero = open("myTest.txt", 'w')
fichero.writelines(lista) # escribe todos los elementos de una lista, los saltos de lineas los debes meter tu en la lista
fichero.close()

'''
Ejercicio opcional: 
Escribir dos funciones que nos permitan interactuar con ficheros:
escribir("mensaje")
leer() # una vez leido borra el contenido del fichero
'''
