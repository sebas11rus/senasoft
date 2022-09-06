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
        
    
    # tipo_doc = forms.ChoiceField(
    #     label='tipo documento', widget=forms.Select(choices=tipo_doc))
    # num_doc = forms.IntegerField(label='numero documento')
    # nombre = forms.CharField(label='nombre', max_length=50)
    # apellido = forms.CharField(label='apellido', max_length=50)
    # sexo = forms.ChoiceField(label='sexo', widget=forms.Select(choices=sexo))
    # celular = forms.CharField(label='celular')
    # telefono = forms.IntegerField(label='telefono')
    # municipio = forms.CharField(label='municipio', max_length=50)
    # direccion = forms.CharField(label='direccion', max_length=50)
    # fecha_nac = forms.DateField(label='fecha de nacimiento')
    # etnia = forms.CharField(label='etnia', max_length=50)
    # discapacidad = forms.CharField(label='discapacidad', max_length=50)
    # estrato = forms.IntegerField(label='estrato')
    # acceso_tec = forms.ChoiceField(
    #     label='acceso a dispositivos moviles', widget=forms.Select(choices=acceso_tec))
    # cuales = forms.CharField(label='cuales', max_length=100)
    # conectividad = forms.ChoiceField(
    #     label='cuenta con acceso a internet', widget=forms.Select(choices=conectividad))
    # regimen = forms.ChoiceField(label='regimen de afiliacion', widget=forms.Select(choices=regimen)) 
