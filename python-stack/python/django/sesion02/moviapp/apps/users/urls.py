from django.urls import path

from . import views

urlpatterns =[
    path('', views.index),
    #path('register', views.register),
    path('register', views.register, name = 'registro'),
    #path('register_user', views.registro_usuario),
    path('home', views.home_usuario),
    path('logout', views.logout),
    path('checkEmail', views.checkEmail)
]