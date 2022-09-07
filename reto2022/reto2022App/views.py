from django.shortcuts import render
from registroApp.models import Sondeo
# Create your views here.

def index(request):
    sondeos = Sondeo.objects.all()
    return render(request,'index.html', {'sondeos': sondeos})