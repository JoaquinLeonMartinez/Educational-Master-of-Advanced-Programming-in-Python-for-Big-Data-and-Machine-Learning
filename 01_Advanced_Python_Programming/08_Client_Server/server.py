# Clase 8 Programacion Avanzada: Servicios de red y Aplicaciones web

import socket

# Sockets

# creamos el servidor:
# El primer parametro indica el tipo de peticion que acepta y el segundo el protocolo (mirar docu si quiero saber mas)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 & tcP (SON LOS EQUIVALENTES A LOS VALORES INDICADOS)
# Creamos un puerto cualquiera
port = 1234
# Vinculamos este puerto a nuestro socket (bind nos permite vincular una direccion IP a un puerto)
s.bind(('',port)) # Con esto le indicamos que acepte todo tipo de conexiones
print(f'Socket vinculado al puerto {port}')

# Ponemos el servidor en modo escucha y le indicamos el nº de conexiones simultaneas que acepta
s.listen(5)

while True:
    # Inicia una conexion con el cliente (c es la conexion con el cliente)
    c, addr = s.accept()
    print(f'Inicia la conexion con el cliente {addr}')
    
    # Enviamos un mesaje al cliente desde el servidor
    c.send("Hola soy el servidor".encode("utf-8"))
    
    c.close()

