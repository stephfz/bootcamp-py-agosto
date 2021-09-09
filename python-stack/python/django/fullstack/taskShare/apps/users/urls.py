from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('home', views.home),
    path('logout', views.logout),
    path('settings', views.settings),
    path("task" , views.task),
]