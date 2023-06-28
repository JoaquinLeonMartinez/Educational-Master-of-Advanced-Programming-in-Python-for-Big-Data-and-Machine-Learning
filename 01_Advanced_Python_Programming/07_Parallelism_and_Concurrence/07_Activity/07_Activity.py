'''
Author: Joaquin Leon Martinez

Crea un script el cual mediante la librería threading o _thread permita ejecutar una funcion simple 
(por ejemplo una función con un print) con diferentes hebras.

'''

from time import sleep
from threading import Thread, current_thread, Semaphore
import random

'''
En este ejercicio vamos a simular una carrera en la que los participantes tendran un nombre unico de corredor.
En la carrera habra dos zonas criticas, en la primera de ellas solo pueden entrar 5 a la vez y 
en la segunda solo 1 porque sera donde se registre la posicion de llegada a la meta.
Se esperara a que todos terminen para printar el podio.
'''

max_competitors_in_main_zone = 5
main_zone_time = 0.5
semaforo = Semaphore(max_competitors_in_main_zone) 
semaforoFinal = Semaphore(1)
position=0
podio = "TOP 10 COMPETITORS\n"

names = ["Rayo", "Perro", "Gato", "Atropello", "Martillo", "Tiburon", "Mamporrero", "Afilador", 
         "Tornado", "Huracan", "Camello", "Ventilador", "Loquillo", "Huron", "Ciclista", "Programador",
         "Alfarero", "SantaClaus", "Mariano Rajoy", "Pianista"]
adjetives = ["rojo", "amarillo", "verde", "turquesa", "magenta", "arruinado", "forrado", "triste", 
             "hiperactivo", "narizudo", "ciego", "tuerto", "dixlesico", "añejo", "profundo", "cojo"]

def region_critica(id):
    with semaforo: # Si no utilizasemos el semaforo se pisarian los valores de x
        print(f"El corredor {current_thread().getName()} ({id}) entra en la zona critica")
        sleep(main_zone_time)
        print(f"El corredor {current_thread().getName()} ({id}) sale de la zona critica")


def goal(id):
    with semaforoFinal:
        global position
        position += 1
        print(f"El corredor {current_thread().getName()} ({id}) finaliza la carrera la carrera en la posicion {position}")
        if position <= 10:
            global podio
            podio += f"{position} - {current_thread().getName()} ({id})\n"

def entrar_a_la_carrera(id):
    print(f"El corredor {current_thread().getName()} ({id}) comienza la carrera")
    sleep(1)
    region_critica(id)
    sleep(1)
    goal(id)
    
    
competitors = [] 
for n in range(0,100):
    if len(names) > 0:
        randomNamePos = random.randint(0, len(names)-1)
        t = Thread(target = entrar_a_la_carrera, args= (n,), name= f"{names[randomNamePos]} { adjetives[random.randint(0, len(adjetives)-1)]}")
        competitors.append(t)
        t.start()
        names.pop(randomNamePos)

# Esperamos a que todos acaben para ver el podio
for competitor in competitors:
    competitor.join()
    
print(podio)

