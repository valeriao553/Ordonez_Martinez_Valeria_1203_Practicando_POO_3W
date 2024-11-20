print(" ")
print("Ordonez Martinez Valeria")
print(" ")
class Marino:
    def hablar(self):
        print("Hola soy un animal marino!")

class Delfin(Marino):
    def hablar(self):
        print("Hola soy un delfin!")

class Ballena(Marino):
    def hablar(self, mensaje):
        print(mensaje)

# Creating instances and calling the hablar method
marino = Marino()
marino.hablar()

pulpo = Delfin()
pulpo.hablar()

foca = Ballena()
foca.hablar("Hola soy una Ballena!")
