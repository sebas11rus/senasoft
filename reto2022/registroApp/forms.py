from django import forms


tipo_doc = [
    ('C.C', 'cedula de ciudadania'),
    ('T.I', 'tarjeta de identidad'),
    ('C.E', 'cedula extranjera')
]


class RegistroForm(forms.Form):
    tipo_doc = forms.CharField(label='tipo documento', max_length=100)
    num_doc = forms.IntegerField(label='numero documento', max_length=12)
