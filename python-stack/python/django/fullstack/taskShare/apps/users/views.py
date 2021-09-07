from django.core.checks import messages
from .models import User, UserManager
from django.shortcuts import render, redirect
from .forms.customForms import LoginForm


import bcrypt
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else: # "POST"  
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/register')    
        else:
            name = request.POST['name']
            last_name = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            encrypted_pwd = make_password(password)

            new_user = User.objects.create(name = name, lastname = last_name, 
                                email = email, password = encrypted_pwd)
            print('Nuevo Usuario: ', new_user.name) 
            request.session['logged_userid'] = new_user.id  
            request.session['logged_username'] = new_user.name
            return redirect('/home')                 


def login(request):
    if request.method == "GET":
        loginForm = LoginForm()
        context  = {'loginForm' : loginForm}
        return render(request, 'login.html' ,  context = context)
    else: #POST / autenticacion
        loginForm = LoginForm( request.POST )
        if loginForm.is_valid():
            user = loginForm.login(request.POST)
            if user:
                print("logged user: ", user)
                request.session['logged_userid'] = user.id
                request.session["logged_username"] = user.name
                return redirect('/home')
        #return render(request, 'login.html') 
        return redirect('/login')        



def home(request):
    try:
        user = User.objects.get(id = int(request.session["logged_userid"]))
        if user:
            return render(request, 'home.html')
        else:
            return redirect('/')    
    except:
        return redirect('/')    


def logout(request):
    try: 
        del request.session['logged_username']
        del request.session['logged_userid']
    except:
        print('Error')
    return redirect('/')        

