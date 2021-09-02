from contextlib import ContextDecorator
from typing import ContextManager
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render

from .models import Actor, User, Movie, Director

from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else: # method == POST
        #creacion de un usuario
        name = request.POST['name']
        lastname = request.POST['lastname']
        correo_electronico = request.POST['email']
        password = request.POST['password']

        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/register_user')    
        else:
            new_user =User.objects.create(name = name, lastname = lastname, 
                        email= correo_electronico, password = password)
            print('Usuario Creado: ', new_user.name)

            request.session['username'] = new_user.name
            return redirect('/home') 

def home(request):
    return render(request, 'home.html')

def register_movie(request):
    if request.method == 'GET':
        return render(request, 'movie.html')

    

def movies(request):
    if request.method == 'GET':
        all_movies = Movie.objects.all() #Movie Catalog
        all_directors = Director.objects.all()
        all_actors = Actor.objects.all()
        context = {'movies': all_movies, 'directors': all_directors, 'actors': all_actors}
        return render(request, 'movies.html', context)
    else: #"POST"
        title = request.POST['title']
        description = request.POST['description']
        release_date = request.POST['release_date'] 
        duration = request.POST['duration'] 

        #el registro de nueva pelicula requiere un director 
        director_id = int(request.POST['director']) #del select
        print ('director_id: ', director_id)
        director = Director.objects.get(id = director_id)
        print ('Director --> ', director.first_name)

        #obtener actores seleccionados
        checked_actors_id = request.POST.getlist('actor')
        print('checked_actors_id---> ', checked_actors_id)
        actors = Actor.objects.filter(pk__in = checked_actors_id)
        print('actors---> ', actors)


        #registrar nueva pelicula con director asociado
        new_movie = Movie.objects.create(title = title, description = description,
                            release_date= release_date, duration = duration, director=director)

        #agregar actores a new_movie
        for actor in actors:
            new_movie.actors.add(actor)

        print ("Nueva Pelicula: ", new_movie.title)
        return redirect('/movies')   

def movie(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    context = {'movie': movie}
    return render(request, 'movie.html', context)

def director(request):
    if request.method == 'GET':
        all_directors = Director.objects.all()
        context = {'directors': all_directors}
        return render(request, 'directors.html', context)
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nationality = request.POST['nationality']  
        new_director = Director.objects.create(first_name = first_name, last_name= last_name,
                                nationality = nationality) 
        print ('Nuevo Director: ', new_director.first_name)
        return redirect('/director')      

def director_movies(request, director_id):
    director = Director.objects.get(id = director_id)
    context = {'director': director}
    return render(request, 'director.html', context)

