from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), #ruta del index
    path('home_usuario', views.home_usuario),
    path('hola_usuario/<str:username>', views.hello_user),
    path('repeticiones/<str:username>/<int:repeticiones>', views.repetir)

]