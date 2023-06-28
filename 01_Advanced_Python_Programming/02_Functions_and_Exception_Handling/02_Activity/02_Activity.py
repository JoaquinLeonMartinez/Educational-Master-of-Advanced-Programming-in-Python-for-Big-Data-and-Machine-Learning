'''
Author: Joaquin Leon Martinez

Escribe una función que acepte dos variables numéricas y calcule la suma y
la resta de dichas cifras. La función devolverá tanto la suma como la resta.
Utiliza las excepciones para controlar algún posible error dentro de la
función.
Crea una función en la cual el segundo parámetro sea un argumento
predeterminado. Ejemplo de llamada:
Mifuncion(20,30)
Mifuncion(20)
'''

def sumayresta(a,b):
    try:
        return a+b, a-b
    except Exception as e:
        print(f"Recuerda que ambos parametros deben ser numericos melon. Ha ocurrido el siguiente error: {e}")
    
print(sumayresta(6,7))

def funcionPred(a,b=30):
    print(f"los parametros indicados son {a} y {b}")
    
funcionPred(20, 40)
funcionPred(20)