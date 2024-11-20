print(" ")
print("Ordonez Martinez Valeria")
print(" ")
class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, Nombre, nombre, edad):
        Universidad.__init__(self, Nombre)
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad}. Estudio en la preparatoria de {self.Nombre}")

# Creating an instance of Estudiante
persona = Estudiante("Cbtis 128", "Valeria", 16)
persona.carrera("Programacion")
persona.datos()
print(" ")
