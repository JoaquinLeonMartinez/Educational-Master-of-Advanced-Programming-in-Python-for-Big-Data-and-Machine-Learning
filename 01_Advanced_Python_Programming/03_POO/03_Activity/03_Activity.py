'''
Author: Joaquin Leon Martinez

Crea una clase calculadora que pueda ser utilizada de la siguiente manera:
calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()
'''

class Calculadora:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def sumar(self):
        return self.num1 + self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def dividir(self):
        try:
            return self.num1 / self.num2
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

calculadora = Calculadora(3,4)

print("El resultado de la suma es", calculadora.sumar())
print("El resultado de la resta es", calculadora.restar())
print("El resultado de la multiplicacion es", calculadora.multiplicar())
print("El resultado de la division es", calculadora.dividir())
