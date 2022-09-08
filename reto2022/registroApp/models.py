
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ciudadano(models.Model):

    TIPO_DOC = (
        ('C.C', 'cedula de ciudadania'),
        ('T.I', 'tarjeta de identidad'),
        ('C.E', 'cedula extranjera'),
    )

    SEXO = (
        ('H', 'Hombre'),
        ('F', 'Femenino'),
        ('IN', 'intersexual'),
        ('IND', 'Indifinido'),
        ('PRE', 'Prefiere no decir'),
    )

    DISPOSITIVOS = (
        ('S', 'Si'),
        ('N', 'No'),
    )

    CUALES = (
        ('M', 'Movil'),
        ('C', ' Computador'),
        ('T', 'Tablet'),
        ('O', 'Otro'),
    )

    CONECTIVIDAD = (
        (True, 'Si'),
        (False, 'No'),
    )

    REGIMEN = (
        ('SUB', 'Subsidiado'),
        ('CON', 'Contributivo'),
    )

    tipo_doc = models.CharField(max_length=20, choices=TIPO_DOC)
    n_doc = models.IntegerField()
    nom = models.CharField(max_length=30)
    ape = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15, choices=SEXO)
    cel = models.CharField(max_length=20, blank=True)
    tel = models.IntegerField(blank=True)
    mun = models.CharField(max_length=30)
    dire = models.CharField(max_length=30, blank=True)
    barrio = models.CharField(max_length=30)
    fecha_nac = models.DateField(auto_now_add=False)
    etnia = models.CharField(max_length=30)
    disc = models.CharField(max_length=30)
    estrato = models.IntegerField()
    accs_tec = models.CharField(
    max_length=30, default=True, choices=DISPOSITIVOS)
    cuales = models.CharField(max_length=50, choices=CUALES)
    con_int = models.BooleanField(default=True, choices=CONECTIVIDAD)
    reg = models.CharField(max_length=30, choices=REGIMEN)
    usuario = models.CharField(max_length=50)
    
    def __str__(self):
        ciudadano = '%s %s cel: %s ' % (self.nom, self.ape,self.cel)
        return ciudadano

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=250)

    def __str__(self):
        return self.pregunta

class Condicion(models.Model):
    brr = models.CharField(max_length=50)
    edad = models.IntegerField()
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
    hora_c = models.TimeField(auto_now=False, auto_now_add=False)
    img = models.ImageField(upload_to="sondeo/", blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
    id_ciudadano = models.ManyToManyField(Ciudadano)

    def __str__(self):
        sondeo = '%s %s' %(self.tematica, self.hora_c)
        
        return sondeo
        
class Certificado(models.Model):
    fecha_gen = models.DateTimeField(auto_now_add=True)
    id_sondeo = models.ForeignKey(Sondeo, on_delete=models.CASCADE)

    def __str__(self):
        certificado = '%s %s %s' % (Ciudadano.nombre, Ciudadano.ape, Ciudadano.updated)
        return certificado