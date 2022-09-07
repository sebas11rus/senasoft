from django.urls import path
from . import views



urlpatterns = [
    path('', views.RegistroUser.as_view(), name='autenticacion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
     
]

