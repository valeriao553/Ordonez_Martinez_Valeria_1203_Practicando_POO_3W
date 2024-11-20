print(" ")
print("Ordonez Martinez Valeria")
print(" ")

class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        
        print(self.nombre + " " + self.apellido)

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
     
        print(self.carrera)


estudiante = Estudiante("Valeria", "Ordoñez", "Medicina")
estudiante.nombre_completo()  
estudiante.mostrar_carrera()  
