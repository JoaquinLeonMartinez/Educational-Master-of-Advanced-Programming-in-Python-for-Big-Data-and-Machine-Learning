# Clase 3 Programacion Avanzada: Clases y objetos (POO)

class Gato:
    
    # Atributos de clase
    especie = "mamifero"
    
    # Atributos de instancia
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    # Metodos
    def hablar(self):
        print(f"Hola soy {self.nombre}")
    
    def scratch(self):
        print(f"Te esta atacando {self.nombre}")
    

gato1 = Gato("Manuelin", "Amarillo")
gato2 = Gato("Mochilo", "Azul")

print(gato1.nombre)
print(gato1.especie)
gato1.scratch()
gato2.hablar()

class Clase:
    # Metodos de instancia:
    def metodoDeInstancia(self):
        print("Example method")
    
# Pueden acceder y modificar los atributos de un objeto
# Pueden acceder a otros metodos
# Puede modificar el estado de la clase

    # Metodos de clase: (al final estos son mas restrictivos por un tema de seguridad)
    @classmethod #Esto es un decorador que indica que este metodos es un metodo de clase
    def metodoDeClase(cls):
        print(cls)
# No puede acceder a los atributos de instancia, solo a los de clase
# Puede modificar los atributos de clase

    # Metodos estaticos: No pueden modificar ni los atributos de clase ni de instancia
    @staticmethod
    def metodoEstatico():
        print("metodo estatico")
        
metodoEjemplo = Clase()

metodoEjemplo.metodoDeInstancia()
Clase.metodoDeClase()