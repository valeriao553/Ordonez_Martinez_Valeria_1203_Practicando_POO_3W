class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
        print("OBJETO = carro")

# Creating instances and printing details
moto = Moto(4, "Blanco", "$50,000")
moto.cantidad()

print("OBJETO = Carro")

carro = Carro(4, "Negro", "$60,000")
carro.cantidad()
