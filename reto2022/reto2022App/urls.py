from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contestar/', views.contestar, name='contestar'),
    path('', views.error, name='error'),
    path('reporte/', views.Generar_pdf.as_view(), name='reporte'),
]
