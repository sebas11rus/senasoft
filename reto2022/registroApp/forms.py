from django import forms


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

class RegistroForm(forms.Form):
    tipo_doc = forms.CharField(
        label='tipo documento', widget=forms.Select(choices=tipo_doc))
    num_doc = forms.IntegerField(label='numero documento', max_length=12)
    nombre = forms.CharField(label='nombre', max_length=50)
    apellido = forms.CharField(label='apellido', max_length=50)
    sexo = forms.CharField(label='sexo', widget=forms.Select(choices=sexo))
    celular = forms.CharField(label='celular')
    telefono = forms.IntegerField(label='telefono')
    municipio = forms.CharField(label='municipio', max_length=50)
    direccion = forms.CharField(label='direccion', max_length=50)
    fecha_nac = forms.DateField(label='fecha de nacimiento' max_length=50)
    etnia = forms.CharField(label='etnia', max_length=50)
    discapacidad = forms.CharField(label='discapacidad', max_length=50)
    estrato = forms.IntegerField(label='estrato')
    acceso_tec = forms.CharField(
        label='acceso a dispositivos moviles', widget=forms.Select(choices=acceso_tec))
    cuales = forms.CharField(label='cuales', max_length=100)
    conectividad = forms.CharField(
        label='cuenta con acceso a internet', widget=forms.Select(choices=conectividad))
    regimen = forms.CharField(label='regimen de afiliacion', widget=forms.Select(choices=regimen)) 
