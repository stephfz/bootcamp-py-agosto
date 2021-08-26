
from django.urls import path

from . import views
urlpatterns =[
    path('', views.index),
    path('register_user', views.register_user),
    path('home', views.home)
]