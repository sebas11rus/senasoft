from django.urls import path
from . import views



urlpatterns = [
    path('', views.RegistroUser.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
     
]

