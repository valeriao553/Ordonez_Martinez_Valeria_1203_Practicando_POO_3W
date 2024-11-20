print(" ")
print("Ordonez Martinez Valeria")
print(" ")
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1


p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))


p.cumpleaños()

print(f"El proximo año {p.nombre} cumple {p.edad} años")
