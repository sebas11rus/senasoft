from django.contrib import admin
from .models import Certificado,Ciudadano,Condicion,Pregunta,Sondeo
# Register your models here.

admin.site.register(Condicion)
admin.site.register(Pregunta)
admin.site.register(Sondeo)