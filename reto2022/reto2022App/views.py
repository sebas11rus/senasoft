from django.shortcuts import render
from registroApp.models import Sondeo
# Create your views here.

def index(request):
    sondeos = Sondeo.objects.all()
    return render(request,'index.html', {'sondeos': sondeos})

def contestar(request):
    sondeos = Sondeo.objects.filter(visible=True, )
    return render(request, 'contestar.html', {'sondeos': sondeos})

def error(request):
    return render(request, 'error.html')