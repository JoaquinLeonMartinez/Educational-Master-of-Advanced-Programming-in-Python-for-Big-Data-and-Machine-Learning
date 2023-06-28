import socket

# creamos el socket del cliente
s = socket.socket()

port = 1234

# Para conectarnos indicamos la IP (local host o 127.0.0.1) y el puerto
s.connect(('127.0.0.1', port))

# Recibimos el mensaje del servidor

# Se indica la cantidad maxima de bytes que se quieren recibir y se decodifica (todo lo que se envie debe estar codificado)
data = s.recv(1024).decode("utf-8") 
s.close
print(f"Recibimos el mensaje: {data}")