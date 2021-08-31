
from django.urls import path

from . import views
urlpatterns =[
    path('', views.index),
    path('register_user', views.register_user),
    path('home', views.home),
    path('register_movie', views.register_movie),
    path('movies', views.movies),
    path('director', views.director),
    path('director_movies/<int:director_id>', views.director_movies)
]