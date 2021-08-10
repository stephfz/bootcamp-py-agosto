#print("Hola desde archivo")


apellido = 'Frias'

#print ("Hola " + nombre + " " + apellido)

#print ("Hola {} {}".format(nombre,apellido))



#invocando a la funcion
#print (saludo(nombre))  

mayoria_edad = 18

def mayor_de_edad(edad):
    if (edad >= mayoria_edad):
        return("eres mayor de edad")
    else:
        annios_faltantes = mayoria_edad - edad
        return("te faltan : {} annios para ser mayor de edad".format(annios_faltantes)) 


def saludo(nombre,edad):
    print ("Hola {}, {}".format(nombre, mayor_de_edad(edad)))


nombre = "Stephanie"
edad = 12
#saludo(nombre, edad)

def suma_producto(a,b):
    suma = a + b
    producto = a * b
    return suma, producto

#print (suma_producto(2,5))    


cadena = "ABCD"
maximo = len(cadena)
#print (maximo)

# indices inician en 0
#for k in range(0,maximo):
    #print(cadena[k])


#for k in range(0, maximo, 2):
    #print(cadena[k])

#for k in range(maximo - 1, -1 , -1):
#    print(cadena[k])  

'''
colores = ["rojo", "verde", "azul", 12]

for color in colores:
    print(color)
'''    

menu = {'lunes' : 'pasta' , 
        'martes' : 'pizza', 
        'miercoles': 'pescado'}

#print (menu.keys())

#print(menu['lunes'])

print (menu.values())

'''
for k in menu.keys():
    print(menu[k])
'''

#for k in menu.values():
#    print(k)

menu = {'lunes' : 'pasta' , 
        'martes' : 'pizza', 
        'miercoles': 'pescado',
        'jueves': ['vegetales', 'papa']}

#for k in menu.values():
#    print(k)        

print(menu['jueves'][0])