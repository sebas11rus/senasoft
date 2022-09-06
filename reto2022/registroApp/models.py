
from django.db import models

# Create your models here.

class Ciudadano(models.Model):
    GENERO= (('M', 'Masculino'),
             ('F', 'femenino'))
    tipo_doc =  models.CharField(max_length=3)
    n_doc = models.IntegerField()
    nom = models.CharField(max_length=30)
    ape= models.CharField(max_length=50)
    sexo = models.CharField(max_length=15, choices=GENERO)
    cel = models.CharField(max_length=20)
    tel = models.IntegerField()
    mun = models.CharField(max_length=30)
    dire = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    fecha_nac = models.DateField(auto_now_add=False)
    etnia = models.models.CharField( max_length=30)
    disc = models.CharField(max_length=30)
    estrato = models.models.IntegerField()
    accs_tec= models.CharField(max_length=30)
    cuales = models.CharField(max_length=50)
    con_int = models.models.BooleanField()
    reg = models.CharField(max_length=30)
    

class Certificado(models.Model):
    a
    
    
    