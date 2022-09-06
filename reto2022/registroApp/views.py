from django.shortcuts import render
from .forms import RegistroForm
from .models import Ciudadano

# Create your views here.


def registro(request):
   form= RegistroForm()
   return render(request, 'registro.html', {'form': form})


def GuardarRegistro(request):
    form= Ciudadano(request.POST)