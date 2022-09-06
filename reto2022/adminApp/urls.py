from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrador, name="administrador"),
    path('nuevaPregunta/', views.nuevaPregunta, name="nuevaPregunta"),
]
