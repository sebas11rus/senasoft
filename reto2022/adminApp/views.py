from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from registroApp.models import Pregunta


# Create your views here.

def administrador(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'admin.html')
    else:
        return render(request, 'error.html')


def nuevaPregunta(request):
    if request.method == 'POST':
        pregunta = Pregunta(request.POST or None)        
        pregunta=Pregunta.cleaned_data['pregunta']
        pregunta.save()
        return HttpResponse('Guardado correctamente')    
    return render(request, 'nuevaPregunta.html')
