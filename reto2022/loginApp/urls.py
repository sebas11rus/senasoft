from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.RegistroUser.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
     
]

