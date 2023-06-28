# Clase 1 Programacion Avanzada: Trabajando con colecciones

# Sets: 
# No admite repetidos y los ordena automaticamente
# (por lo que se dice que son desordenados porque no mantiene el orden original)
# Sus elemetos son inmtables, no se pueden modificar una vez creados
'''
miConjunto1 = set([2,7,5,3,5])
miConjunto1 = {2,7,5,3,5} # Lo mismo que antes pero mas rapido
print(miConjunto1)
print(type(miConjunto1))

# Operaciones

#Lo puedes recorrer con un bucle

for i in miConjunto1:
    # Esto no se podria --> print(miConjunto[i])
    print(i)
    
miConjunto2 = {7,1,9,5,3,5}

print(miConjunto1 | miConjunto2) # Pinta la union de ambos conjuntos

# Add element
miConjunto1.add(9)

# Remove element
miConjunto1.remove(2) # Si no existe da error

miConjunto1.discard(2) # Este lo borraria y no daria error si no esta

miConjunto1.pop() # Elimina un elemento aleatorio

#miConjunto1.clear() # Lo vacia

# Otras operaciones:
print(miConjunto1.union(miConjunto2))
print(miConjunto1.intersection(miConjunto2))
# Hay un monton mas, mirar la docu
'''
# Tuplas (menos restrictivas que los set pero mas que las listas)
#  No se pueden modificar una vez declaradas
# Permite duplicados
'''
miTupla1 = (2,3,2,6)
miTupla2 = (2,3,2,(4,5)) # Puede haber arrays dentro de las tuplas
print(miTupla1)
print(miTupla1[2])
print(miTupla2[3][1]) # Accedemos al segundo valor del elemento 3
print(miTupla1.count(2)) # Numero de veces que hay un elemento
'''

# Listas
# Permite cualquier tipo de dato
# Son indexadas
# Se pueden anidar
# Son mutables
# Son dinamicas

miLista1 = [2,3,5,2,6]
'''
print(miLista1[0]) # Obtener el primer elemento
print(miLista1[-1]) # Obtener el ultimo elemento
print(miLista1[-3]) # Obtener el tercero por atras
print(miLista1[-3:]) # Obtener los ultimos 3 elementos
print(miLista1[:3]) # Obtener todos hasta el tercero

miLista2 = [2,True,["Hola", (3,4,5)]]

print(miLista2[2][1][1])

# add element
miLista1.append(2)

# extender una lista 
miLista1.extend([2,3,4])
miLista1.extend(miLista2)

# add element en una posicion determinada
miLista1.insert(2,2) # posicion, valor

# eliminar un elemento
miLista1.remove(2) # Si no existe obtenemos un error

#eliminar el ultimo elemento
miLista1.pop()

# invertir una lista
miLista1.reverse()

# ordenar una lista
miLista1.sort(reverse=True)

# obtener un indice desde su primera ocurencia
miLista1.index(2) # Dvuelve la posicion de la primera aparicion del valor 2

miLista1.index(2,5) # Lo mismo pero empieza a buscar a partir de la posicion 5
'''
# Ejercicios:
# Crear tablas de multiplicar mediante listas
# Contar los elementos duplicados de un conjunto

# Clase extra: 

# Diccionarios
# Son dinamicos
# Son anidados
# Son indexados

d1 = {
    "clave1": 2,
    "clave2": True,
    "clave3": 34
}

# Otra forma de declararlo pero que no se suele utilizar
d2 = {
    ("rojo","coche"),
    ("azul",23)
    }
print(d1["clave1"])
print(d1.get("clave1"))

d1["clave1"] = "Mariano"
print(d1["clave1"])

# Recorrer el diccionario
for i in d1:
    print(d1[i])

# Si queremos obtener tanto la clave como el valor
for x,y in d1.items():
    print(x,y)
    
# Diccionarios anidados:
d1_anidado = {
    "Nombre": "Luis"
}

d2_anidado = {
    "Nombre": "Maria"
}

d3_anidado = {
    "d1": d1_anidado,
    "d2":d2_anidado
}

# Devolver un listado de Keys y values
it = d1.items()
print(it)
print(list(it))

# Obtener todas las keys en una lista
print(list(d1.keys()))
# Obtener todas los valores en una lista
print(list(d1.values()))

# Eliminar elemento
d1.pop("clave7", -1) # Si no existe la key nos devolvera -1 en lugar de error
d1.popitem() # elimina un item aleatorio

# Actualiar un valor si hay un martch con una key o añadirlo en caso de n oexistir la key

d1_anidado = {
    "a": 1,
    "b": 2
}

d2_anidado = {
    "c": 1,
    "b": 5
}

d1_anidado.update(d2_anidado) # Ahora d1_anidado tendra tambien el valor c y se habra actualizado la b

print(d1_anidado)

# Ejemplo carrito de la compra:
mi_carrito = ["platanos", "manzanas"]

stock ={
    "platanos":34,
    "manzanas":23
}

precios = {
    "platanos": 2.3,
    "manzanas": 1.35
}

def pasar_por_caja(lista_compra):
    total_pago = 0
    for elemento in lista_compra:
        precio = precios[elemento]
        if stock[elemento] > 0:
            total_pago += precio
            stock[elemento] -= 1
    return total_pago
    

resultado = pasar_por_caja(mi_carrito)
print(resultado)
print(stock)