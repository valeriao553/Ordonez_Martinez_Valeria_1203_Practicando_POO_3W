print(" ")
print("Ordonez Martinez Valeria")
print(" ")
class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO!")
        else:
            print("Has REPROBADO!")

estudiante1 = Estudiante("Alexa", 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Valeria", 10)
estudiante2.imprimir()
estudiante2.resultados()
