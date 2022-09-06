from django.shortcuts import render
from .forms import RegistroForm
from .models import Ciudadano

# Create your views here.


def registro(request):
    ciudadano = Ciudadano.objects.all()
    return render(request, 'registro.html', {'ciudadano': ciudadano})
