from django.urls import path
from . import views


urlpatterns = [
    path('', views.registro, name='registro'),
    # path('reporte/', views.get, name='reporte'),

]
