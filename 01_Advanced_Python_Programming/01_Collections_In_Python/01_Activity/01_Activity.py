'''
Author: Joaquin Leon Martinez

Listas: Utiliza una lista para almacenar los números del 1 al 10 la cual debe ser rellenada 
con el uso de un bucle while. Finalmente muestra la lista en orden inverso. 

Diccionarios:
1.Crea un diccionario con 4 valores.
2.Muestra los valores del diccionario.
3.Modifica el 3º valor del diccionario
4.Añade un nuevo valor al diccionario de tipo lista
5.Muestra nuevamente los valores
'''

# Listas
maxLen = 10
lista = []
i = 0

# Llenar lista
while i < maxLen:
    i += 1
    lista.append(i)

#Mostrar lista

i=0
while i < len(lista):
    i += 1
    print(lista[-i])
    
# Diccionarios

#1.Crea un diccionario con 4 valores.
d1 = {
    "key1":1,
    "key2":3,
    "key3":3,
    "key4":4
}

#2.Muestra los valores del diccionario.
it = d1.items()
print(list(d1.values()))

#3.Modifica el 3º valor del diccionario
# Caso en el que sabemos la clave de la tercera posicion:
d1["key3"] = 5
# Mostramos
it = d1.items()
print(list(d1.values()))

# Caso en el que no sabemos el valor de la tercera clave
it = d1.items()
d1[list(d1.keys())[2]] = 9
# Mostramos:
it = d1.items()
print(list(d1.values()))

#4.Añade un nuevo valor al diccionario de tipo lista
dExtra = {
    "extra": (2,3)
}

d1.update(dExtra)

#5.Muestra nuevamente los valores

it = d1.items()
print(list(d1.values()))