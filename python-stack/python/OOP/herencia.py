
class Vehiculo():
    __annioFabricacion = ''

    def __init__(self, num_ruedas):
       self.num_ruedas = num_ruedas

    def setAnnioFabricacion(self, annio):
        self.__annioFabricacion = annio

    def getAnnioFabricion(self):
        return self.__annioFabricacion

    def __str__(self):
        return ("Soy un vehiculo de {} ruedas".format(self.num_ruedas))     


class Moto(Vehiculo):
    def __init__(self, num_ruedas):
        super().__init__(num_ruedas)    


class Trailer(Vehiculo):
    __tonalaje = 0

    def __init__(self, num_ruedas, toneladas):
        super().__init__(num_ruedas)
        self.__tonalaje = toneladas

    def getTonelaje(self):
        return self.__tonalaje    

    def setTonelaje(self, toneladas):
        self.__tonalaje = toneladas


moto = Moto(2)
trailer = Trailer(8, 1000)

print(moto)
print(trailer)

trailer.setAnnioFabricacion('2010')
print(trailer.getAnnioFabricion())