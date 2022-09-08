from django import forms
from .models import Ciudadano


tipo_doc = [
    ('C.C', 'cedula de ciudadania'),
    ('T.I', 'tarjeta de identidad'),
    ('C.E', 'cedula extranjera'),
]

sexo = [
    ('mas', 'masculino'),
    ('fem', 'femenino'),
]


acceso_tec = [
    ('si', 'si'),
    ('no', 'no'),
]


conectividad = [
    ('si', 'si'),
    ('no', 'no'),
]


regimen = [
    ('sub', 'subsidiado'),
    ('cont', 'contributivo'),
]

class RegistroForm(forms.ModelForm):
    
    class Meta:
        model = Ciudadano
        fields = ('tipo_doc', 'n_doc','nom','ape','sexo','cel','tel','mun',
                  'dire','barrio','fecha_nac','etnia','disc',
                  'estrato','accs_tec','cuales','con_int','reg')
        
    
