from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import re

def index(request):
    print ('metodo: ', request.method)
    return render(request, 'index.html')

'''
def register(request):
    print ('metodo: ', request.method)
    return render(request, 'register.html')   

def registro_usuario(request): #POST
    print ('metodo: ', request.method)
    #print(request.POST)
    print(request.POST['username'])
    print(request.POST['email'])
    request.session['usuario_registrado'] = request.POST['username']
    request.session['email'] = request.POST['email']
    #return render(request, 'index.html') 
    #return redirect('/') 
    return redirect('/home')  
'''

# Mejorando y limpiando codigo
def register(request):
    if request.method == 'GET':
        print ("...Solicitud GET")
        return render(request, 'register.html')
    else: #no es GET, es POST 
        print('...Solicitud POST')
        request.session['usuario_registrado'] = request.POST['username']
        request.session['email'] = request.POST['email']
        return redirect('/home')   



def home_usuario(request):
    #usuario = request.POST['username']
    #print(usuario)    
    try: 
        if request.session['usuario_registrado']:
            print ('usuario: ', request.session['usuario_registrado'])
            context = {'usuario' : request.session['usuario_registrado'],
                        'email': request.session['email']}
            return render(request, 'home.html', context)
    except:
        print('Error')
    return render(request, 'index.html')    


def logout(request):
    try:
        del request.session['usuario_registrado']
    except:
        print('Error')
    return redirect("/")  
    

def checkEmail(request): 
    errors = {}
    data = request.POST['email']
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(data):
        errors['email'] = 'Correo Invalido'
    print ('Validando Correo:  ', errors)
    err = JsonResponse({'errors' : errors})
    return  err   