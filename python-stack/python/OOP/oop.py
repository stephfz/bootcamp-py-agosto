perro = { 
            "nombre" : "Avellana",
            "edad" : 4,
            "raza" : "cocker",
            "tamano" : "Mediano"
}

perro2 = { 
            "nombre" : "Choco",
            "edad" : 4,
            "raza" : "cocker",
            "tamano" : "Grande"
}

class Perro:

    def __init__(self, nombre, edad, raza, tamanio = "Pequeno"):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.tamanio = tamanio

    def sentarse(self):
        print("Estoy sentado")

    def __str__(self):
        return ("Me llamo {}, tengo {} annios y soy de tamanio {}".format(self.nombre, self.edad, self.tamanio))      

mascota = perro("Chocolate", 3, "cocker")      
mascota.sentarse()
mascota.nombre = "OtroNombre"
print (mascota.nombre) 
print (mascota.tamanio) 
print(mascota)