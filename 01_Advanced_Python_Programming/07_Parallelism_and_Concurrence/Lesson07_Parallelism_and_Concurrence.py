# Clase 7 Programacion Avanzada: Paralelismo y concurrencia

from time import sleep, perf_counter
from threading import Thread, current_thread, Semaphore

def task():
    sleep(1)
    
def task2(id):
    print(f"Entramos en el hilo {id}")
    print(current_thread().getName())
    sleep(1)

'''
Ejemplo sin concurrencia

def task():
    sleep(1)
    
start = perf_counter()

task()
task()
task()
task()

finish = perf_counter()

print(f"Tiempo total sin concurrencia = {finish-start}")
'''



'''
Ejemplo con concurrencia 1

start = perf_counter()

# Inicializar hilos:
thread1 = Thread(target = task)
thread2 = Thread(target = task)
thread3 = Thread(target = task)
thread4 = Thread(target = task)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Esperamos a que acaben los hilos:

thread1.join()
thread2.join()
thread3.join()
thread4.join()

finish = perf_counter()
print(f"Tiempo total con con currencia = {finish-start}")

'''

# Ejemplo con concurrencia 2 (ahora con parametros)
'''
start = perf_counter()

hilos = []

for n in range(0,10):
    t = Thread(target = task2, args= (n,), name= "hilo_"+str(n))
    hilos.append(t)
    t.start()
    
for t in hilos:
    t.join()
    
finish = perf_counter()
print(f"Tiempo total con con currencia = {finish-start}")

'''
# Semaforos:

semaforo = Semaphore(1)# Se indica el numero de hilos que pueden acceder a la vez

def region_critica(id):
    with semaforo: # Si no utilizasemos el semaforo se pisarian los valores de x
        global x
        x = x + id
        print(f"El hilo {id} vale {x}")
        x = 1

x = 1

for n in range(0,10):
    t = Thread(target = region_critica, args= (n,), name= "hilo_"+str(n)).start()  


