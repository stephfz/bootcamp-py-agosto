from django.shortcuts import render


def index(request):
    return render(request,"index.html")

#enrutamiento 
def home_usuario(request):
    return render(request,'home_usuario.html')    

#enrutamiento con parametro
def hello_user(request , username):
    context = {'username_HTML': username}
    return render(request, 'hola_usuario.html', context)


def repetir(request, username, repeticiones):
    context = {'username_HTML': username, 'repeticiones_HTML' : range(repeticiones)}
    return render(request, 'repeticiones.html', context)