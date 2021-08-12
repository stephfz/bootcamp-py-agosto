class Persona():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre}")  
        #print("Hola mi nombre es {}".format(self.nombre))

class Instructor(Persona):

    def __init__(self, nombre, email, curso):
        super().__init__(nombre, email)
        self.curso = curso

    def saludar(self):
        #super().saludar() 
        return("Mi nombre es {} y soy Instructor de {}".format(self.nombre, self.curso))   


class Estudiante(Persona):

    def __init__(self, nombre, email, cohort):
        super().__init__(nombre, email)
        self.cohort = cohort

    def saludar(self):
        super().saludar() 
        print("Soy Estudiante del cohort de {}".format(self.cohort))      


class Bootcamp():
    __listaEstudiantes = []

    def __init__(self, nombre, zoom_link, instructor):
        self.nombre = nombre
        self.zoom_link = zoom_link
        self.instructor = instructor

    def getInstructorBootcamp(self):
        return self.instructor.saludar()

    def agregarEstudiante(self, estudiante):
        self.__listaEstudiantes.append(estudiante)

    def getEstudiantes(self):
        for estudiante in self.__listaEstudiantes:
            estudiante.saludar()



ins = Instructor(nombre = "Stephanie", curso = "Python",  email = "sfrias@codingdojo.cl")
est = Estudiante("Maria", "m.gomex@mail.com", "Agosto2021")
est2 = Estudiante("Ana", "m.ana@mail.com", "Agosto2021")

#ins.saludar()
#est.saludar()

bootcamp_Agosto = Bootcamp("Python Full Stack", "link", ins)
print ("Nombre del Bootcamp:" , bootcamp_Agosto.nombre)
print(bootcamp_Agosto.getInstructorBootcamp())
bootcamp_Agosto.agregarEstudiante(est)
bootcamp_Agosto.agregarEstudiante(est2)
print("------")
bootcamp_Agosto.getEstudiantes()