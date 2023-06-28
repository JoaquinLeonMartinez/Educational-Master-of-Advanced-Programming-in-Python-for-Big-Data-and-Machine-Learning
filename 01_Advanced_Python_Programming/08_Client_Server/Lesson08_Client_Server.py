# Clase 8 Programacion Avanzada: Servicios de red y Aplicaciones web

#Ejemplo 1: Usar sockets para hacer un servidor y un cliente (mirar los ficheros client.py y server.py)

#Ejemplo2: Montar web con FLASK

from flask import Flask # No lo pilla porque el corrector no es el del env

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola mundo"

@app.route("/contacto")
def contacto():
    return "Hola desde el contacto"

@app.route("/noticia/<string:noticia>")
def noticia(noticia):
    return f"Hola desde la noticia: {noticia}"


# Windows:
# set FLASK_APP=Clase8Main.py
# flask --app Clase8Main.py --debug run

# MAC
# export FLASK_APP = "Clase8Main.py"