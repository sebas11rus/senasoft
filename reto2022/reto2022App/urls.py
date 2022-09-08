from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('contestar/', views.contestar, name='contestar'),
    path('', views.error, name='error'),
]
