print(" ")
print("Ordonez Martinez Valeria")
print(" ")
class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2  
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        if self._num2 != 0:  
            resultado = self._num1 // self._num2
            print(f"El resultado de la división es: {self._num1} // {self._num2} = {resultado}")
        else:
            print("No se puede dividir por cero.")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")
num1 = int(input("Ingrese un nuemro: "))
num2 = int(input("Ingrese segundo numero: "))
print(" ")
operacion = Calculadora(num1, num2)
operacion.suma()

operacion = Calculadora(num1, num2)
operacion.resta()

operacion = Calculadora(num1, num2)
operacion.division()


operacion = Calculadora(num1, num2)
operacion.multiplicacion()
