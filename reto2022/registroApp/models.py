
from django.db import models

# Create your models here.


class Ciudadano(models.Model):
    GENERO = (('M', 'Masculino'),
              ('F', 'femenino'))
    tipo_doc = models.CharField(max_length=3)
    n_doc = models.IntegerField()
    nom = models.CharField(max_length=30)
    ape = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15, choices=GENERO)
    cel = models.CharField(max_length=20)
    tel = models.IntegerField()
    mun = models.CharField(max_length=30)
    dire = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    fecha_nac = models.DateField(auto_now_add=False)
    etnia = models.models.CharField(max_length=30)
    disc = models.CharField(max_length=30)
    estrato = models.models.IntegerField()
    accs_tec = models.CharField(max_length=30)
    cuales = models.CharField(max_length=50)
    con_int = models.models.BooleanField()
    reg = models.CharField(max_length=30)


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=50)


class Condicion(models.Model):
    brr = models.CharField(max_length=50)
    edad = models.models.IntegerField()
    grupo_p = models.CharField(max_length=50)


class Sondeo (models.Model):
    tipo = models.CharField(max_length=25)
    fecha_p = models.DateField(auto_now=False, auto_now_add=False)
    hora_p = models.TimeField(auto_now=False, auto_now_add=False)
    visible = models.BooleanField(default=True)
    tematica = models.CharField(max_length=25)
    fecha_c = models.DateField(auto_now=False, auto_now_add=False)
    hora_c = models.TimeField(auto_now=False, auto_now_add=False)
    img = models.ImageField()
